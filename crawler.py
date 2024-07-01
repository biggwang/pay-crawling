# google_play_scraper에서 필요한 기능과 정렬 방식을 가져옵니다.
from datetime import datetime
import webclient
import scraper


# 수집하고자 하는 특정 기간 설정
start_date = datetime(2024,5,7)
end_date = datetime(2024,5,8)

# 수집된 리뷰 데이터를 저장할 리스트 초기화 
reviews_data = []


# 수집된 리뷰에 대해 반복하며 필요한 정보를 리스트에 저장
result = scraper.get_reviews()
# app_store_scraper.get_review()


for item in result:
    print(item['content'])

webclient.send_message("#crawling", '오늘의 목소리')
