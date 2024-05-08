# google_play_scraper에서 필요한 기능과 정렬 방식을 가져옵니다.
from google_play_scraper import Sort, reviews_all
from datetime import datetime
import requests


# 'lang'은 리뷰를 가져올 언어를 설정합니다. 여기서는 'ko'로 설정하여 한국어 리뷰를 가져옵니다.
lang = 'ko'

# 'cont'는 리뷰를 가져올 국가를 설정합니다. 여기서는 'kr'로 설정하여 한국에서의 리뷰를 가져옵니다.
cont = 'kr'


# reviews_all 함수를 사용해 앱의 리뷰를 모두 가져옵니다. 이 예에서는 'com.hanbit.rundayfree'라는 앱의 리뷰를 가져옵니다.
result = reviews_all(
    'com.kakaopay.app',
    sleep_milliseconds=3000, # 리뷰를 가져오는 사이의 대기 시간을 설정합니다. 0으로 설정하여 대기하지 않습니다.
    lang=lang, # 리뷰의 언어를 설정합니다. 여기서는 위에서 설정한 'ko'(한국어)입니다.
    country=cont, # 리뷰를 가져올 국가를 설정합니다. 여기서는 위에서 설정한 'kr'(한국)입니다.
    sort=Sort.MOST_RELEVANT, # 리뷰를 어떤 기준으로 정렬할지 설정합니다. 가장 관련성 높은 순으로 정렬합니다.
    filter_score_with=5 #평점이 5점인 리뷰만 크롤링
)


# 수집하고자 하는 특정 기간 설정
start_date = datetime(2024,5,7)
end_date = datetime(2024,5,8)

# 수집된 리뷰 데이터를 저장할 리스트 초기화
reviews_data = []

# 수집된 리뷰에 대해 반복하며 필요한 정보를 리스트에 저장
for item in result:
    print(item['content'])

print("### 슬랙 발송 시작")



def notice_message(token, channel, text, attachments):
    attachments = json.dumps(attachments) # 리스트는 Json 으로 덤핑 시켜야 Slack한테 제대로 간다.
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": text ,"attachments": attachments})

# 생성한 웹훅 주소
Token = 'xoxb-6379869257104-7102812393874-ABOuWNnEidAzm9umizyytU9M'
str1_title = '오늘의 증시 KOSPI 2021-09-17 (금)'
str2 = 'test 메시지를 보냅니다.'

attach_dict = {
    'color' : '#ff0000',
    'author_name' : 'Slack Bot Notice',
    'title' : str1_title,
    'title_link' : 'http://finance.naver.com/sise/sise_index.nhn?code=KOSPI',
    'text' : str1_title,
    'image_url' : 'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png?sidcode=1632301488333'
} # attachment 에 넣고싶은 목록들을 딕셔너리 형태로 입력



attach_list=[attach_dict] # 딕셔너리 형태를 리스트로 변환
notice_message(Token, "#crawling", str2, attach_list)

print("### 슬랙 발송 완료")

