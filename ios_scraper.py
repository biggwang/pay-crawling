from app_store_scraper import AppStore
from datetime import datetime
from pprint import pprint

def get_ios_reviews(keywords):
    kakao_pay = AppStore(country="kr", app_name="kakaopay", app_id="847268987")
    kakao_pay.review(how_many=30)
    
    filtered_reviews = []

    for item in kakao_pay.reviews:
        review_text = item['review'].lower()
        if any(keyword.lower() in review_text for keyword in keywords):
            ##pprint(item['review'])
            filtered_reviews.append(item['review'])
    
    return filtered_reviews
