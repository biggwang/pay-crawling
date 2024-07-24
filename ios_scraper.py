from app_store_scraper import AppStore
from datetime import datetime
from pprint import pprint

def get_reviews(keywords):
    kakao_pay = AppStore(country="kr", app_name="kakaopay", app_id="847268987")
    kakao_pay.review(how_many=30)
    
    filtered_reviews = []

    for item in kakao_pay.reviews:
        review_text = item['review'].lower()
        if any(keyword.lower() in review_text for keyword in keywords):
            filtered_review = {
                'date': item['date'].strftime('%y-%m-%d %H:%M:%S'),
                'review': item['review'],
                'rating': item['rating']
            }
            filtered_reviews.append(filtered_review)
    
    return filtered_reviews
