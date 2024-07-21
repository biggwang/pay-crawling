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


def get_reviews(keywords):
    # review_all = reviews_all(
    #         'com.kakaopay.app',
    #         sleep_milliseconds=3000,
    #         lang='ko',
    #         country='kr',
    #         num=1000,
    #         sort=Sort.NEWEST,
    # )

    result, continuation_token  = reviews(
            'com.kakaopay.app',
            lang='ko',
            country='kr',
            count=10,
            sort=Sort.NEWEST,
    )

    num_reviews = len(result)
    print(f"######### Number of reviews fetched: {num_reviews} {continuation_token}")

    # Filter the desired fields from each review
    filtered_reviews = [
        {'content': review['content'], 'at': review['at'], 'score': review['score']}
        for review in result
    ]

    # Print the filtered reviews
    return filtered_reviews

