from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass


class EmailSender(object):
    def __init__(
            self,
            event: str,
    ) -> None:
        events = {'kbaseball': '국내야구', 'wbaseball': '해외야구', 'kfootball': '국내축구', 'wfootball': '해외축구',
                    'basketball': '농구', 'volleyball': '배구', 'golf': '골프', 'general': '일반', 'esports': 'e스포츠 & 게임'}

        self.event = events[event]
        self.subject = events[event] + ' 뉴스를 전달해드리겠습니다.'
        self.from_email_id = 'seomk9896@gmail.com'
        self.from_email_pw = getpass.getpass(self.from_email_id + "'s password: ")
        self.to_email = 'seomk9896@gmail.com'  # 여러 명 일 때는 리스트 형태로 표현
        self.basic_text = '오늘 하루도 화이팅 하시고, 많은 피드백 부탁드립니다 !\n\n'

    def __call__(self, body):
        message = MIMEMultipart()

        message['Subject'] = self.subject
        message['From'] = self.from_email_id
        message['To'] = self.to_email

        message.attach(MIMEText(self.basic_text, "plain"))
        message.attach(MIMEText(body, "html"))
        msg_body = message.as_string()

        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(message['From'], self.from_email_pw)
        server.sendmail(message['From'], message['To'], msg_body)

        print(self.event + ' 뉴스를 전달하였습니다.')
        server.quit()