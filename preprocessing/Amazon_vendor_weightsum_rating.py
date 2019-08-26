import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def Amazon_vendor_weightsum_rating():
    A_vendor_weigh = pd.read_csv('Amazon_5weeks.csv')

    # 데이터 타임으로 변경
    A_vendor_weigh['Date'] = pd.to_datetime(A_vendor_weigh.loc[:, 'Date'])

    # 두 컬럼만 불러오기
    A_vendor_weigh = A_vendor_weigh[['Date', 'Vendor']]

    # 내림차순으로 정렬
    A_vendor_weigh = A_vendor_weigh.sort_values(['Date'], ascending=[False])

    # 데이트 뉴, 앞으로 설정
    A_vendor_weigh = A_vendor_weigh.set_index('Date')

    # 주차별로 멀티 인덱스 만들기
    A_vendor_weigh1 = A_vendor_weigh.groupby(['Vendor', 'Date']).resample('w').count().unstack()

    # 결측값 = 0 처리
    A_vendor_weigh1 = A_vendor_weigh1.fillna(0)

    # 데이트 뉴 행으로 합치기
    A_vendor_weigh2 = A_vendor_weigh1.sum(axis=1, level='Date')

    # 주+벤더별 정렬하기
    A_vendor_weigh3 = A_vendor_weigh2.sum(axis=0, level='Vendor')

    # 칼럼명 변경
    A_vendor_weigh3.columns = ["Week30", "Week31", "Week32", "Week33", "Week34"]

    # 가중치 더해서 weight_sum하기
    A_vendor_weigh3["Week34"] = A_vendor_weigh3["Week34"] * (0.95)
    A_vendor_weigh3["Week33"] = A_vendor_weigh3["Week33"] * (0.90)
    A_vendor_weigh3["Week32"] = A_vendor_weigh3["Week32"] * (0.85)
    A_vendor_weigh3["Week31"] = A_vendor_weigh3["Week31"] * (0.80)
    A_vendor_weigh3["Week30"] = A_vendor_weigh3["Week30"] * (0.75)

    # 칼럼명으로 오름차순 정렬

    A_vendor_weigh3 = A_vendor_weigh3.sort_index(axis=1, ascending=True)

    ####################################################
    #####주차별 가중치합 (기존의 Weight_sum과 달리, 2~4주차치만 뽑은 데이터!)

    A_vendor_weigh3['Weight_sum'] = A_vendor_weigh3['Week34'] + A_vendor_weigh3['Week33'] + A_vendor_weigh3['Week32'] + \
                                    A_vendor_weigh3['Week31'] + A_vendor_weigh3['Week30']

    # 내림차순으로 정렬
    A_vendor_weigh3 = A_vendor_weigh3.sort_values(["Weight_sum"], ascending=[False])

    # Weight_sum탈락시키기
    A_vendor_weigh3_review_count = A_vendor_weigh3.drop(A_vendor_weigh3.columns[-1:], axis='columns')

    Amazon_Rating = pd.read_csv('Amazon_5weeks_rating.csv')

    Amazon_Rating = Amazon_Rating.drop(Amazon_Rating.columns[0], axis='columns')

    Amazon_Rating = Amazon_Rating[['Samsung', 'Xiaomi', 'OPPO', 'Vivo', 'Realme', 'Huawei', 'Others']]

    Amazon_Rating = np.transpose(Amazon_Rating)

    rating_vendor = A_vendor_weigh3_review_count * Amazon_Rating.values

    ####################################################
    #####주차별 가중치합 (기존의 Weight_sum과 달리, 2~4주차치만 뽑은 데이터!)

    rating_vendor['Weight_sum'] = rating_vendor['Week33'] + rating_vendor['Week32'] + rating_vendor['Week31'] + \
                                  rating_vendor['Week30']
    # + vendor_weigh_2['Week4']

    # 내림차순으로 정렬
    rating_vendor = rating_vendor.sort_values(["Weight_sum"], ascending=[False])

    # Weight_sum탈락시키기
    rating_vendor_review_count = rating_vendor.drop(rating_vendor.columns[-1:], axis='columns')

    # 벤더 + weigh_sum만 불러오기
    rating_vendor_sum = rating_vendor[['Weight_sum']]

    # [ 삼성*블루 = #0A709A // 샤오미*연한레드 = #F44E54  // 리얼미*오렌지 = #FF9904/// 비보*연노  = #FDDB5E // 연한초록 = #76AD3B,  ,  노랑 = #FDDB5E, #BAF1A1 =연두
    # [ 초록 = #76AD3B, skyblue

    # 파이차트 그리기
    plt.pie(rating_vendor_sum,
            explode=(0.1, 0, 0, 0, 0, 0, 0),
            labels=['Samsung', 'Xiaomi', 'OPPO', 'Vivo', 'Huawei', 'Realme', 'Others'],
            colors=['dodgerblue', '#F44E54', 'green', '#FDDB5E', '#76AD3B', '#FF9904', '#BAF1A1'],
            startangle=180,
            autopct='%1.2f%%')

    plt.rcParams.update({'font.size': 25})
    plt.rcParams['figure.figsize'] = [20, 15]
    plt.axis('equal', fontsize=18)
    plt.title('Amazon Review Share (with rating)', fontsize=40)
    plt.legend(fontsize=20, loc='upper left|')

    plt.show()

    # 백분율 구하기 vendor_weigh_2
    rating_vendor = (rating_vendor[0:20] / rating_vendor[0:20].sum()) * 100

    # 행과 열을 바꾸기
    rating_vendor_per = np.transpose(rating_vendor)
    rating_vendor_per.head()

    # [ 삼성 = 0A709A, 샤오미 = #F44E54, 리얼미 = #76AD3B,  오렌지 = #FF9904,  노랑 = #FDDB5E, #BAF1A1 =연두
    # [ 초록 = #76AD3B, skyblue, #F44E54= 연한 레드계열

    # 누적막대그래프 만들기
    rating_vendor_per.plot.bar(stacked=True, fontsize=25,
                               colors=['dodgerblue', '#F44E54', 'green', '#FDDB5E', '#76AD3B', '#FF9904', '#BAF1A1'],
                               alpha=0.7)

    # Set the title and labels

    plt.rcParams['figure.figsize'] = [15, 13]
    plt.legend(fontsize=22, loc='lower right')
    plt.xlabel('weeks', fontsize=23)
    plt.ylabel('Percentage', fontsize=23)
    plt.title('Amazon Weekly Review Share (with rating)', fontsize=40)

    # show the plot
    plt.show()

    x = rating_vendor_review_count.columns[0:]
    y = rating_vendor_review_count[0:]

    pal = ['dodgerblue', '#F44E54', 'green', '#FDDB5E', '#76AD3B', '#FF9904', '#BAF1A1']
    plt.stackplot(x, y, labels=['Samsung', 'Xiaomi', 'OPPO', 'Vivo', 'Huawei', 'Realme', 'Others'],
                  colors=pal, alpha=0.7)

    plt.title("Amazon Weekly Review Count (with rating)", fontsize=40, fontweight=0, color='black')
    plt.xlabel("Weeks", fontsize=24)
    plt.xticks(fontsize=24)

    plt.ylabel("Review counts", fontsize=24)
    plt.yticks(fontsize=24)

    plt.legend(loc='upper left', fontsize=22)
    plt.show()
