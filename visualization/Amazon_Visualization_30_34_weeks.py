import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def Amazon_Visualization_30_34_weeks():
    am = pd.read_csv("Amazon_5weeks.csv")
    am.head()

    df30 = am.loc[(am['Week'] == 30)]
    df30_count = df30['Vendor'].groupby(df30['Vendor']).count()

    df31 = am.loc[(am['Week'] == 31)]
    df31_count = df31['Vendor'].groupby(df31['Vendor']).count()

    df32 = am.loc[(am['Week'] == 32)]
    df32_count = df32['Vendor'].groupby(df32['Vendor']).count()

    df33 = am.loc[(am['Week'] == 33)]
    df33_count = df33['Vendor'].groupby(df33['Vendor']).count()

    df34 = am.loc[(am['Week'] == 34)]
    df34_count = df34['Vendor'].groupby(df34['Vendor']).count()

    am_count = am['Vendor'].groupby(am['Vendor']).count()

    am_sort = am_count.sort_values(ascending=True)

    # list로 묶어서 출력한 뒤 df30_count, am그룹으로 묶은 갯수 결과 비교해보기
    df_list = [list(df30_count), list(df31_count), list(df32_count), list(df33_count), list(df34_count)]

    df_vendor = pd.DataFrame(df_list, columns=['Huawei', 'OPPO', 'Others', 'Realme', 'Samsung', 'Vivo', 'Xiaomi'],
                             index=None)

    df_vendor = df_vendor[['Others', 'Huawei', 'Realme', 'Vivo', 'OPPO', 'Xiaomi', 'Samsung']]

    result = np.array(df_vendor).T

    am_list = list(am_sort)

    plt.rcParams['figure.figsize'] = [15, 9]
    # 리뷰수가 작->큰 순서로 vendor명 입력
    group_names = ['Others', 'Huawei', 'Realme', 'Vivo', 'OPPO', 'Xiaomi', 'Samsung']
    group_size = am_list
    group_colors = ['#BAF1A1', '#76AD3B', '#FF9904', '#FDDB5E', 'green', '#F44E54', 'dodgerblue']
    # ['#F44E54', 'coral']
    group_explodes = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)

    plt.pie(group_size, explode=group_explodes, labels=group_names, colors=group_colors,
            autopct='%1.2f%%', shadow=True, startangle=90)

    plt.axis('equal')
    plt.title('Amazon Review Count Ratio 30 - 34 weeks', fontsize=20)
    plt.show()

    r = [0, 1, 2, 3, 4]
    raw_data = {'Others': result[0], \
                'Huawei': result[1], \
                'Realme': result[2], \
                'Vivo': result[3], \
                'OPPO': result[4], \
                'Xiaomi': result[5], \
                'Samsung': result[6]}

    df_stack = pd.DataFrame(raw_data)

    totals = [i + j + k + l + m + n + o for i, j, k, l, m, n, o in zip(df_stack['Others'],
                                                                       df_stack['Huawei'], df_stack['Realme'],
                                                                       df_stack['Vivo'], df_stack['OPPO'],
                                                                       df_stack['Xiaomi'], df_stack['Samsung'])]

    Others = [i / j * 100 for i, j in zip(df_stack['Others'], totals)]
    Realme = [i / j * 100 for i, j in zip(df_stack['Huawei'], totals)]
    Huawei = [i / j * 100 for i, j in zip(df_stack['Realme'], totals)]
    Vivo = [i / j * 100 for i, j in zip(df_stack['Vivo'], totals)]
    OPPO = [i / j * 100 for i, j in zip(df_stack['OPPO'], totals)]
    Xiaomi = [i / j * 100 for i, j in zip(df_stack['Xiaomi'], totals)]
    Samsung = [i / j * 100 for i, j in zip(df_stack['Samsung'], totals)]

    barWidth = 0.65
    names = ('30Week', '31Week', '32Week', '33Week', '34Week')

    # Create Bars
    plt.bar(r, Others, color='#BAF1A1', edgecolor='white', width=barWidth,
            label="Others")

    plt.bar(r, Huawei, bottom=Others, color='#76AD3B', edgecolor='white',
            width=barWidth, label="Huawei")

    plt.bar(r, Realme, bottom=[i + j for i, j in zip(Others, Huawei)], color='#FF9904',
            edgecolor='white', width=barWidth, label="Realme")

    plt.bar(r, Vivo, bottom=[i + j + k for i, j, k in zip(Others, Huawei, Realme)],
            color='#FDDB5E', edgecolor='white', width=barWidth, label="Vivo")

    plt.bar(r, OPPO, bottom=[i + j + k + l for i, j, k, l in zip(Others, Huawei, Realme, Vivo)],
            color='green', edgecolor='white', width=barWidth, label="OPPO")

    plt.bar(r, Xiaomi, bottom=[i + j + k + l + m for i, j, k, l, m in zip(Others, Huawei, Realme, Vivo, OPPO)],
            color='#F44E54', edgecolor='white', width=barWidth, label="Xiaomi")

    plt.bar(r, Samsung,
            bottom=[i + j + k + l + m + n for i, j, k, l, m, n in zip(Others, Huawei, Realme, Vivo, OPPO, Xiaomi)],
            color='dodgerblue', edgecolor='white', width=barWidth, label="Samsung")

    plt.title("Amazon 30 - 34 weeks Review Count", loc='left', fontsize=25, fontweight=0, color='black')

    # x축
    plt.xticks(r, names, fontsize=15)
    plt.xlabel("Weeks", fontsize=20)

    # y축
    plt.yticks(fontsize=15)
    plt.ylabel("Review Percentage", fontsize=20)

    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1, fontsize=15)
    plt.rcParams['figure.figsize'] = [15, 9]
    plt.show()

    x = [(str(_) + 'Week') for _ in range(30, 35)]  # x축 label
    y = [result[0], result[1], result[2], result[3], result[4], result[5], result[6]]  # Reivew 갯수 누적

    pal = ['#BAF1A1', '#76AD3B', '#FF9904', '#FDDB5E', 'green', '#F44E54', 'dodgerblue']
    # pal = ["#A20101", "#F44E54", "#FF9904", "#FDDB5E", "#BAF1A1", "#76AD3B", "#0A709A"]
    plt.stackplot(x, y, labels=['Others', 'Huawei', 'Realme', 'Vivo', 'OPPO', 'Xiaomi', 'Samsung'],
                  colors=pal, alpha=0.45)

    plt.title("Amazon 30 - 34 weeks Review Count", loc='left', fontsize=25, fontweight=0, color='black')
    plt.xlabel("Weeks", fontsize=17)
    plt.xticks(fontsize=15)

    plt.ylabel("Review counts", fontsize=17)
    plt.yticks(fontsize=15)

    plt.legend(loc='upper right', fontsize=15)
    plt.rcParams['figure.figsize'] = [15, 9]
    plt.show()
    Samsung = am.loc[(am['Vendor'] == 'Samsung')]
    Samsung.head()

    del Samsung['Unnamed: 0']
    Samsung_count = Samsung['Product_name'].groupby(Samsung['Product_name']).count()

    Samsung.reset_index(inplace=True)
    Samsung.head()

    del Samsung['index']
    Samsung.head()

    # 제품 이름만 불러오기
    Samsung['Series'] = Samsung['Product_name'].str[-3:-2]
    Samsung.head()

    Samsung_count = Samsung['Series'].groupby(Samsung['Series']).count()

    Samsung_list = list(Samsung_count)

    plt.rcParams['figure.figsize'] = [12, 8]
    group_names = ['A_series', 'M_series']
    group_size = Samsung_list
    group_colors = ['dodgerblue', 'green']
    # ['#F44E54', 'coral']
    group_explodes = (0.04, 0.04)

    plt.pie(group_size, explode=group_explodes, labels=group_names, colors=group_colors,
            autopct='%1.2f%%', shadow=True, startangle=150)
    plt.axis('equal')
    plt.title('Amazon Samsung Series Ratio 30 - 34 weeks', fontsize=20)
    plt.show()
