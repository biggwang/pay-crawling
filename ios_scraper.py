from app_store_scraper import AppStore
from datetime import datetime
from pprint import pprint

def convert_datetime_to_str(review):
    if 'date' in review and isinstance(review['date'], datetime):
        review['date'] = review['date'].isoformat()
    return review


def get_ios_reviews():
    kakao_pay = AppStore(country="kr", app_name="kakaopay", app_id="847268987")
    kakao_pay.review(how_many=50)  # Adjust the number as needed
    reviews = [convert_datetime_to_str(review) for review in kakao_pay.reviews]
    print(reviews)
    #response = json.dumps(reviews, indent=4, ensure_ascii=False)