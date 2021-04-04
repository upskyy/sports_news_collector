# Copyright (c) 2021, Sangchun Ha. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
from bs4 import BeautifulSoup


class NewsCrawler(object):
    def __init__(
            self,
            event: str,
            default_url: str = 'https://sports.news.naver.com/',
    ) -> None:
        self.event = event
        self.default_url = default_url

    def __call__(self) -> list:
        news_list = list()

        url_list = self._url_crawling(self.default_url, self.event)
        for url in url_list:
            news = self._news_crawling(url).strip()
            if news is not None and news[:2] != 'if' and len(news) > 150:
                news_list.append(news)

        return news_list

    def _url_crawling(self, default_url: str, event: str) -> list:
        url_list = list()

        html = requests.get(default_url + event + '/index.nhn')
        soup = BeautifulSoup(html.text, 'html.parser')

        news1 = soup.find('ul', class_='home_news_list division')
        news2 = soup.find('ul', class_='home_news_list')

        urls = news1.find_all('a')

        for url in urls:
            href = url.attrs['href']
            if href is not None:
                url_list.append(default_url + href)

        urls = news2.find_all('a')
        for url in urls:
            href = url.attrs['href']
            if href is not None:
                url_list.append(default_url + href)

        return url_list

    def _news_crawling(self, url: str) -> str:
        # 스포츠 종목과 언론사마다 틀이 달라서 한번에 예외처리 하기가 힘들다.
        START_EXCEPTION = []  # 다른 스포츠와 다르게 국내 야구에서는 기자 이름을 맨 뒤에 [xxx 기자] 형태로 사용함.
        END_EXCEPTION = ['▶', '@', '┌']  # 국내 야구에서는 앞부분 사진 이후에 기자 이름 앞에 ⓒ 표시 있음.

        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        all_news = soup.find(id='newsEndContents').text
        start_idx = 0
        end_idx = len(all_news)

        for i in range(len(all_news)):
            if all_news[i] in START_EXCEPTION:
                start_idx = i + 1
            if all_news[i] in END_EXCEPTION:
                end_idx = i
                break

        all_news = all_news[start_idx: end_idx]

        return all_news