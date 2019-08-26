import pandas as pd
from dateutil import parser


# %matplotlib inline 주피터용

# Product_name의 첫 음절이 Vendor 명이 아닌 경우를 처리하는 def
def add_vendor_column(dataframe):
    vendor_column = []
    # 6가지의 주요 vendor만 볼거임
    MAJOR = ['Huawei', 'Samsung', 'Xiaomi', 'Vivo', 'OPPO', 'Realme']

    for product_name in dataframe['Product_name']:

        vendor_name = product_name.split()[0]
        if vendor_name == 'Redmi':
            vendor_name = 'Xiaomi'
        if vendor_name == 'Mi':
            vendor_name = 'Xiaomi'
        if vendor_name == 'Honor':
            vendor_name = 'Huawei'
        if vendor_name == 'POCO':
            vendor_name = 'Xiaomi'
        if vendor_name == 'OnePlus':
            vendor_name = 'OPPO'

        if vendor_name in MAJOR:
            vendor_column.append(vendor_name)
        else:
            vendor_column.append('Others')
    dataframe['Vendor'] = vendor_column


# 비오, 규민팀에 주기위해 Point column 변형한 column만드는 과정(현재 process에는 필요없음)
def add_point_new_column(dataframe):
    point_list = []
    for point in dataframe['Point']:
        # Honor -> Huawei
        point_new = point
        if point_new == 1.0:
            point_new = 'Negative'

        if point_new == 2.0:
            point_new = 'Negative'

        if point_new == 3.0:
            point_new = 'Neutral'

        if point_new == 4.0:
            point_new = 'Positive'

        if point_new == 5.0:
            point_new = 'Positive'

        point_list.append(point_new)
    dataframe['Point_new'] = point_list


def Amazon_preprocessing():
    # 아마존에서 받은 csv파일 불러옴
    Amazon = pd.read_csv("reviews0820.csv")

    print(Amazon.shape)

    # 24 July 2019같은 날짜 형태(str)를 datetime형식으로 변경
    parser_date = []
    for i in Amazon['Date']:
        parser_date.append(parser.parse(i).strftime('%Y-%m-%d'))

    Amazon['Date_new'] = parser_date

    Amazon['Date'] = pd.to_datetime(Amazon.loc[:, 'Date_new'])
    Amazon['Date'].head()

    # datetime으로 변경한 Date column으로 week과 year column 생성
    Amazon['Week'] = Amazon['Date'].dt.week

    parser_year = []
    for i in Amazon['Date_new']:
        parser_year.append(parser.parse(i).strftime('%y'))

    Amazon['Year'] = parser_year

    add_point_new_column(Amazon)

    Amazon = Amazon.loc[Amazon['Year'] == '19']

    df30 = Amazon.loc[(Amazon['Week'] == 30)]
    df31 = Amazon.loc[(Amazon['Week'] == 31)]
    df32 = Amazon.loc[(Amazon['Week'] == 32)]
    df33 = Amazon.loc[(Amazon['Week'] == 33)]

    Amazon_new = pd.concat([df30, df31, df32, df33])

    Amazon_new_count = Amazon_new['Vendor'].groupby(Amazon_new['Vendor']).count()

    Amazon_finish_real = Amazon_new[
        ['Vendor', 'Product_name', 'Date', 'Week', 'Year', 'Point', 'Point_new', 'Vote', 'Title', 'Review']]

    Amazon_finish_real.to_csv("Amazon_3033_segonii.csv")
