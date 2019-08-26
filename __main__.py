from crawler.bestSeller import get_bestSeller
from crawler.information import information
from crawler.review import review
from crawler.crawler import *

def crawler():
    # 걸리는 시간 체크
    start_time = time.time()
    information_option = 1
    now = datetime.date.today()
    month_ago = now - datetime.timedelta(days=36)
    date = [month_ago, now]
    print(date)
    #
    # 오늘 날짜 폴더 생성, 시작 지점 날짜 저장(크롤링 중 날짜 넘어가는거 막기위함)
    my_mkdir()

    # 오늘 날짜 확인
    get_current_date()

    # 베스트 셀러 링크 파일 생성하기
    get_bestSeller()

    # 제품 목록 만들기
    information(information_option)

    review(date)

    # 리뷰 목록 파일 생성하기
    # review_page(driver_path)

    print("--- %s seconds ---" % (time.time() - start_time))

def preprocessing():
    pass

def main():
    crawler()
    preprocessing()


if __name__ == '__main__':
    main()