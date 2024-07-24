# google_play_scraper에서 필요한 기능과 정렬 방식을 가져옵니다.
from datetime import datetime
import webclient
import scraper
import ios_scraper


# 수집하고자 하는 특정 기간 설정
start_date = datetime(2024, 6, 23, 0, 0, 0)
end_date = datetime(2024, 7, 23, 23, 59, 59)


print('############################# aos 시작 #############################')
aos_result = scraper.get_reviews(['송금', '쓰레기'], start_date, end_date)
print(aos_result)
print('############################# aos 종료 #############################')



print('############################# ios 시작 #############################')
ios_result = ios_scraper.get_reviews(['송금', '쓰레기'], start_date, end_date)
print(ios_result)
print('############################# ios 종료 #############################')


result = aos_result + ios_result
print(result)


webclient.send_message("#crawling", result)
