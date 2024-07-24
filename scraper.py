from google_play_scraper import Sort, reviews_all, reviews

def get_reviews_filtered(keywords):
    review_all = reviews_all(
            'com.kakaopay.app',
            sleep_milliseconds=3000,
            lang='ko',
            country='kr',
            sort=Sort.NEWEST,
            #filter_score_with=5 #평점이 5점인 리뷰만 크롤링        
    )

    filtered_reviews = []

    for item in review_all:
        review_text = item['content'].lower()
        if any(keyword.lower() in review_text for keyword in keywords):
            filtered_reviews.append(item['content'])

    return filtered_reviews


def get_reviews(keywords, start_date, end_date):
    result, continuation_token  = reviews(
            'com.kakaopay.app',
            lang='ko',
            country='kr',
            count=10,
            sort=Sort.NEWEST,
    )

    num_reviews = len(result)
    print(f"######### Number of reviews fetched: {num_reviews} {continuation_token}")

    filtered_reviews = [
        {
            'content': review['content'],
            'at': review['at'].strftime('%y-%m-%d %H:%M:%S'),
            'score': review['score']
        }
        for review in result
        if any(keyword.lower() in review['content'].lower() for keyword in keywords)
        and start_date <= review['at'] < end_date
    ]

    return filtered_reviews

