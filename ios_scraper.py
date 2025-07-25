# from app_store_scraper import AppStore
# from datetime import datetime
# from pprint import pprint
#
# def get_reviews(keywords, start_date, end_date):
#     kakao_pay = AppStore(country="kr", app_name="kakaopay", app_id="1464496236")
#     kakao_pay.review(how_many=10)
#
#     filtered_reviews = []
#
#     for item in kakao_pay.reviews:
#         review_date = item['date']
#         if start_date <= review_date <= end_date:
#             review_text = item['review'].lower()
#             if any(keyword.lower() in review_text for keyword in keywords):
#                 filtered_review = {
#                     'date': item['date'].strftime('%y-%m-%d %H:%M:%S'),
#                     'review': item['review'],
#                     'rating': item['rating']
#                 }
#                 filtered_reviews.append(filtered_review)
#
#     return filtered_reviews


import requests
import json
from pprint import pprint

# 앱 ID와 요청 URL 설정
app_id = "1464496236"  # 카카오페이 앱의 실제 ID
page = 1
url = f"https://itunes.apple.com/kr/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json"

# 요청 보내기
response = requests.get(url)
if response.status_code != 200:
    print("리뷰 데이터를 가져오지 못했습니다.")
    exit()

# JSON 데이터 파싱
data = response.json()
entries = data.get('feed', {}).get('entry', [])

# 리뷰가 하나도 없는 경우
if not entries:
    print("리뷰가 없습니다.")
else:
    for entry in entries:
        author = entry.get('author', {}).get('name', {}).get('label', '')
        title = entry.get('title', {}).get('label', '')
        content = entry.get('content', {}).get('label', '')
        rating = entry.get('im:rating', {}).get('label', '')
        version = entry.get('im:version', {}).get('label', '')
        updated = entry.get('updated', {}).get('label', '')

        print("작성자:", author)
        print("별점:", rating)
        print("제목:", title)
        print("내용:", content)
        print("앱 버전:", version)
        print("작성일:", updated)
        print("-" * 50)
