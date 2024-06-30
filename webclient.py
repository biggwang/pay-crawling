import requests
import json
import os


def send_message(channel, title):
    print("### 슬랙 발송 시작")
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + os.getenv('SLACK_URL')},
        data={
            "channel": channel, 
            "text": title 
            })
    print(response.status_code)
    print("### 슬랙 발송 종료")


def send_message_with_attach(channel, title, attachments):
    print("### 슬랙 발송 시작")
    attachments = json.dumps(attachments) # 리스트는 Json 으로 덤핑 시켜야 Slack한테 제대로 간다.
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + os.getenv('SLACK_URL')},
        data={
            "channel": channel, 
            "text": title ,
            "attachments": attachments
            })
    print(response.status_code)
    print("### 슬랙 발송 종료")