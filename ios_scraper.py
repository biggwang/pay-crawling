from app_store_scraper import AppStore
from datetime import datetime
from pprint import pprint

def get_reviews(keywords, start_date, end_date):
    kakao_pay = AppStore(country="kr", app_name="kakaopay", app_id="1464496236")
    kakao_pay.review(how_many=10)
    
    filtered_reviews = []

    for item in kakao_pay.reviews:
        review_date = item['date']
        if start_date <= review_date <= end_date:
            review_text = item['review'].lower()
            if any(keyword.lower() in review_text for keyword in keywords):
                filtered_review = {
                    'date': item['date'].strftime('%y-%m-%d %H:%M:%S'),
                    'review': item['review'],
                    'rating': item['rating']
                }
                filtered_reviews.append(filtered_review)
    
    return filtered_reviews
