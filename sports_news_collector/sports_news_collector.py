from sports_news_collector.news_crawler import NewsCrawler
from sports_news_collector.email_sender import EmailSender
from pororo import Pororo
from pandas import DataFrame
from pretty_html_table import build_table
import pandas as pd
import datetime


class SportsNewsCollector(object):
    def __init__(
            self,
            event: str,
            lang: str = 'ko',
            default_url: str = 'https://sports.news.naver.com/',
    ) -> None:
        self.lang = lang.lower()

        self.default_url = default_url
        self.summary = Pororo(task='summarization', model='abstractive', lang=self.lang)
        self.sentiment_analysis = Pororo(task="sentiment", model="brainbert.base.ko.nsmc", lang=self.lang)

        if event in self.available_events():
            self.event = event
        else:
            raise KeyError('Unknown events : {}, available events are {}'.format(event, self.available_events()))

    def collect(self) -> None:
        collector = NewsCrawler(self.event, self.default_url)
        news_list = collector()

        news_info = self._make_news_info(news_list)

        sender = EmailSender(self.event)
        sender(news_info)

    def _make_news_info(self, news_list: list) -> DataFrame:
        datetime_list = list()
        sentiment_list = list()
        summary_list = list()
        news_info = {'datetime': datetime_list, 'sentiment': sentiment_list, 'summary': summary_list}

        date = str(datetime.datetime.now())
        date = date[:-7]

        for idx in range(len(news_list)):
            datetime_list.append(date)

            summary = self.summary(news_list[idx])
            summary_list.append(summary)
            sentiment_list.append(self.sentiment_analysis(summary))

        news_info = pd.DataFrame(news_info)
        news_info = build_table(news_info, 'orange_light')

        return news_info

    @staticmethod
    def available_events() -> list:
        return ['kbaseball', 'wbaseball', 'kfootball', 'wfootball', 'basketball', 'volleyball', 'golf', 'general', 'esports']


