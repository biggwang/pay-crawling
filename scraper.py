from google_play_scraper import Sort, reviews_all



def get_reviews():
    # 'lang'은 리뷰를 가져올 언어를 설정합니다. 여기서는 'ko'로 설정하여 한국어 리뷰를 가져옵니다.
    lang = 'ko'
    # 'cont'는 리뷰를 가져올 국가를 설정합니다. 여기서는 'kr'로 설정하여 한국에서의 리뷰를 가져옵니다.
    cont = 'kr'

    # reviews_all 함수를 사용해 앱의 리뷰를 모두 가져옵니다. 이 예에서는 'com.hanbit.rundayfree'라는 앱의 리뷰를 가져옵니다.
    return reviews_all(
        'com.kakaopay.app',
        sleep_milliseconds=3000, # 리뷰를 가져오는 사이의 대기 시간을 설정합니다. 0으로 설정하여 대기하지 않습니다.
        lang=lang, # 리뷰의 언어를 설정합니다. 여기서는 위에서 설정한 'ko'(한국어)입니다.
        country=cont, # 리뷰를 가져올 국가를 설정합니다. 여기서는 위에서 설정한 'kr'(한국)입니다.
        sort=Sort.MOST_RELEVANT, # 리뷰를 어떤 기준으로 정렬할지 설정합니다. 가장 관련성 높은 순으로 정렬합니다.
        filter_score_with=5 #평점이 5점인 리뷰만 크롤링
    )