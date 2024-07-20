from app_store_scraper import AppStore
from datetime import datetime
from pprint import pprint

def get_ios_reviews():
    kakao_pay = AppStore(country="kr", app_name="kakaopay", app_id="847268987")
    kakao_pay.review(how_many=5)
    
    for item in kakao_pay.reviews:
        pprint(item['review'])
