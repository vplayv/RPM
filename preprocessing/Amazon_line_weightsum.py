import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rc

def Amazon_line_weightsum():
    samsung_ms = pd.read_csv('Amazon_5weeks.csv')

    # 데이터 타임으로 변경
    samsung_ms['Date'] = pd.to_datetime(samsung_ms.loc[:, 'Date'])

    # 두 컬럼만 불러오기
    samsung_ms = samsung_ms[['Date', 'Product_name']]

    # 데이트 뉴, 앞으로 설정
    samsung_ms = samsung_ms.set_index('Date')

    # 띄어쓰기 별로 나누고 불러오기
    samsung_ms['Product_name'] = samsung_ms['Product_name'].str.split(' ').str[:3]

    # 삼성제품만 불러오기
    samsung_ms = samsung_ms[samsung_ms['Product_name'].str[0] == 'Samsung']

    # 제품 이름만 불러오기
    samsung_ms['Product_name'] = samsung_ms['Product_name'].str[2]

    # 제품 시리즈만 불러오기
    samsung_ms['Product_name'] = samsung_ms['Product_name'].str[0]

    # 진짜 제품라인으로 이름 변경
    samsung_ms['Product_name'] = samsung_ms['Product_name'].replace('A', 'A series')
    samsung_ms['Product_name'] = samsung_ms['Product_name'].replace('J', 'J series')
    samsung_ms['Product_name'] = samsung_ms['Product_name'].replace('M', 'M series')
    samsung_ms['Product_name'] = samsung_ms['Product_name'].replace('O', 'ON series')
    # samsung_ms['Name'] = samsung_ms['Name'].replace('P','ON series')
    samsung_ms['Product_name'] = samsung_ms['Product_name'].replace('S', 'S series')

    samsung_ms['Product_name'].head()

    # 주차별로 멀티 인덱스 만들기
    a_samsung_ms = samsung_ms.groupby(['Product_name', 'Date']).resample('w').count().unstack()
    a_samsung_ms.head()

    # 결측값 = 0 처리
    a_samsung_ms = a_samsung_ms.fillna(0)
    a_samsung_ms.head()

    # 데이트 뉴 행으로 정렬하기
    a_samsung_ms1 = a_samsung_ms.sum(axis=1, level='Date')

    # 주+벤더별 정렬하기
    a_samsung_ms2 = a_samsung_ms1.sum(axis=0, level='Product_name')
    # 칼럼명 변경
    a_samsung_ms2.columns = ["Week30", "Week31", "Week32", "Week33", "Week34"]

    # 가중치 더해서 weight_sum하기
    a_samsung_ms2["Week34"] = a_samsung_ms2["Week34"] * 0.95
    a_samsung_ms2["Week33"] = a_samsung_ms2["Week33"] * 0.90
    a_samsung_ms2["Week32"] = a_samsung_ms2["Week32"] * 0.85
    a_samsung_ms2["Week31"] = a_samsung_ms2["Week31"] * 0.80
    a_samsung_ms2["Week30"] = a_samsung_ms2["Week30"] * 0.75

    # 칼럼명으로 오름차순 정렬

    a_samsung_ms2 = a_samsung_ms2.sort_index(axis=1, ascending=True)

    ####################################################
    #####주차별 가중치합 (기존의 Weight_sum과 달리, 2~4주차치만 뽑은 데이터!)

    a_samsung_ms2['Weight_sum'] = a_samsung_ms2['Week34'] + a_samsung_ms2['Week33'] + a_samsung_ms2['Week32'] + \
                                  a_samsung_ms2['Week31'] + a_samsung_ms2['Week30']

    # 내림차순으로 정렬
    a_samsung_ms2 = a_samsung_ms2.sort_values(["Weight_sum"], ascending=[False])

    # Weight_sum탈락시키기
    a_samsung_ms2_review_count = a_samsung_ms2.drop(a_samsung_ms2.columns[-1:], axis='columns')

    # csv파일로 저장하기
    data = pd.DataFrame(a_samsung_ms2)
    data.to_csv('Amazon_line_weight_sum.csv')

    # 벤더 + weigh_sum만 불러오기
    A_vendor_weigh3 = a_samsung_ms2[['Weight_sum']]

    # 파이차트 그리기
    plt.pie(A_vendor_weigh3,
            explode=(0.05, 0),
            labels=['M series', 'A series'],
            colors=['green', 'dodgerblue'],
            startangle=180,
            autopct='%1.2f%%')

    plt.rcParams.update({'font.size': 25})
    plt.rcParams['figure.figsize'] = [20, 15]
    plt.axis('equal', fontsize=18)
    plt.title('Amazon Samsung Smartphone Review Share', fontsize=40)
    plt.legend(fontsize=22, loc='upper left')

    plt.show()

    # 백분율 구하기 vendor_weigh_2
    a_samsung_ms2_per = (a_samsung_ms2[0:] / a_samsung_ms2[0:].sum()) * 100

    # csv파일로 저장하기 (주별 리뷰 점유율 percentage)
    data1 = pd.DataFrame(a_samsung_ms2_per)
    data1.to_csv('Weekly_Amazon_line_weight_sum_per.csv')

    # 행과 열을 바꾸기
    a_samsung_ms2_per = np.transpose(a_samsung_ms2_per)
    a_samsung_ms2_per.head()

    # 누적막대그래프 만들기
    a_samsung_ms2_per.plot.bar(stacked=True, fontsize=25,
                               colors=['green', 'dodgerblue'], alpha=0.7)

    # Set the title and labels
    plt.rcParams['figure.figsize'] = [15, 13]
    plt.legend(fontsize=23, loc='lower right')
    plt.xlabel('weeks', fontsize=23)
    plt.ylabel('Percentage', fontsize=23)
    plt.title('Amazon Weekly Samsung Smartphone Review Share ', fontsize=40)

    # show the plot
    plt.show()

    x = a_samsung_ms2_review_count.columns[0:]
    y = a_samsung_ms2_review_count[0:]

    pal = ['green', 'dodgerblue']
    plt.stackplot(x, y, labels=['M series', 'A series'],
                  colors=pal, alpha=0.7)

    plt.title("Amazon Weekly Samsung Smartphone Review Count", fontsize=40, fontweight=0, color='black')
    plt.xlabel("Weeks", fontsize=24)
    plt.xticks(fontsize=24)

    plt.ylabel("Review counts", fontsize=24)
    plt.yticks(fontsize=24)

    plt.legend(loc='upper right', fontsize=22)
    plt.show()
