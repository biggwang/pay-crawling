from app_store_scraper import AppStore
import json

# Initialize the AppStore object with the app's name and country code
kakao_pay = AppStore(country="kr", app_name="카카오페이")

# Get the app details (including the app ID)
kakao_pay.review(how_many=50)  # Set the number of reviews you want to fetch


def get_review():
    # Print the reviews
    for review in kakao_pay.reviews:
        print(f"Title: {review['title']}")
        print(f"Rating: {review['rating']}")
        print(f"Review: {review['review']}")
        print(f"Date: {review['date']}")
        print("-" * 80)