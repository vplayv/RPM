import pandas as pd
import numpy as np
import dateutil
import calendar
#파이차트 라이브러리
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rc
# package to extract data from various Internet sources into a DataFrame
# make sure you have it installed
from pandas_datareader import data, wb

# package for dates
import datetime as dt

def Amzon_vendor_weight_sum():
    A_vendor_weigh = pd.read_csv('Amazon_5weeks.csv')

    # 데이터 타임으로 변경
    A_vendor_weigh['Date'] = pd.to_datetime(A_vendor_weigh.loc[:, 'Date'])

    # 두 컬럼만 불러오기
    A_vendor_weigh = A_vendor_weigh[['Date', 'Vendor']]
    A_vendor_weigh.head()

    # 내림차순으로 정렬
    A_vendor_weigh = A_vendor_weigh.sort_values(['Date'], ascending=[False])

    # 데이트 뉴, 앞으로 설정
    A_vendor_weigh = A_vendor_weigh.set_index('Date')

    # 주차별로 멀티 인덱스 만들기
    A_vendor_weigh1 = A_vendor_weigh.groupby(['Vendor', 'Date']).resample('w').count().unstack()
    A_vendor_weigh1.head()

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

    # csv파일로 저장하기
    data = pd.DataFrame(A_vendor_weigh3)
    data.to_csv('Amazon_vendor_weight_sum.csv')

    # 벤더 + weigh_sum만 불러오기
    A_vendor_weigh4 = A_vendor_weigh3[['Weight_sum']]

    # 파이차트 그리기
    plt.pie(A_vendor_weigh4,
            explode=(0.1, 0, 0, 0, 0, 0, 0),
            labels=['Samsung', 'Xiaomi', 'OPPO', 'Vivo', 'Realme', 'Huawei', 'Others'],
            colors=['dodgerblue', '#F44E54', 'green', '#FDDB5E', '#FF9904', '#76AD3B', '#BAF1A1'],
            startangle=180,
            autopct='%1.2f%%')

    plt.rcParams.update({'font.size': 25})
    plt.rcParams['figure.figsize'] = [20, 15]
    plt.axis('equal', fontsize=18)
    plt.title('Amazon Review Share', fontsize=40)
    plt.legend(fontsize=20, loc='upper right')

    plt.show()
    # 백분율 구하기 vendor_weigh_2
    A_vendor_weigh3_per = (A_vendor_weigh3[0:20] / A_vendor_weigh3[0:20].sum()) * 100

    # csv파일로 저장하기 (주별 리뷰 점유율 percentage)
    data1 = pd.DataFrame(A_vendor_weigh3_per)
    data1.to_csv('weekly_Amazon_vendor_weight_sum_percetage#.csv')

    # 행과 열을 바꾸기
    A_vendor_weigh3_per = np.transpose(A_vendor_weigh3_per)
    A_vendor_weigh3_per.head()

    # 누적막대그래프 만들기
    A_vendor_weigh3_per.plot.bar(stacked=True, fontsize=25,
                                 colors=['dodgerblue', '#F44E54', 'green', '#FDDB5E', '#FF9904', '#76AD3B', '#BAF1A1'],
                                 alpha=0.7)

    # Set the title and labels
    plt.rcParams['figure.figsize'] = [15, 13]
    plt.legend(fontsize=22, loc='lower right')
    plt.xlabel('weeks', fontsize=23)
    plt.ylabel('Percentage', fontsize=23)
    plt.title('Amazon Weekly Review Share', fontsize=40)

    # show the plot
    plt.show()

    x = A_vendor_weigh3_review_count.columns[0:]
    y = A_vendor_weigh3_review_count[0:]

    pal = ['dodgerblue', '#F44E54', 'green', '#FDDB5E', '#FF9904', '#76AD3B', '#BAF1A1']
    plt.stackplot(x, y, labels=['Samsung', 'Xiaomi', 'OPPO', 'Vivo', 'Realme', 'Huawei', 'Others'],
                  colors=pal, alpha=0.7)

    plt.title("Amazon Weekly Review Count", fontsize=40, fontweight=0, color='black')
    plt.xlabel("Weeks", fontsize=24)
    plt.xticks(fontsize=24)

    plt.ylabel("Review counts", fontsize=24)
    plt.yticks(fontsize=24)

    plt.legend(loc='upper right', fontsize=22)
    plt.show()


