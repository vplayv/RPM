import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import seaborn as sns


def Amazon_preprocessing_weight_visual_30_to_34():
    am = pd.read_csv("Amazon_5weeks.csv")
    samsung = am.loc[(am['Vendor'] == 'Samsung')]
    xiaomi = am.loc[(am['Vendor'] == 'Xiaomi')]
    realme = am.loc[(am['Vendor'] == 'Realme')]
    others = am.loc[(am['Vendor'] == 'Others')]
    vivo = am.loc[(am['Vendor'] == 'Vivo')]
    huawei = am.loc[(am['Vendor'] == 'Huawei')]
    oppo = am.loc[(am['Vendor'] == 'OPPO')]

    sam_overall = samsung['Point'].mean()
    xia_overall = xiaomi['Point'].mean()
    real_overall = realme['Point'].mean()
    other_overall = others['Point'].mean()
    vivo_overall = vivo['Point'].mean()
    hua_overall = huawei['Point'].mean()
    oppo_overall = oppo['Point'].mean()

    sam30 = samsung.loc[(samsung['Week'] == 30)]
    sam31 = samsung.loc[(samsung['Week'] == 31)]
    sam32 = samsung.loc[(samsung['Week'] == 32)]
    sam33 = samsung.loc[(samsung['Week'] == 33)]
    sam34 = samsung.loc[(samsung['Week'] == 34)]

    round(sam30['Point'].mean(), 2)
    round(sam31['Point'].mean(), 2)
    round(sam32['Point'].mean(), 2)
    round(sam33['Point'].mean(), 2)
    round(sam34['Point'].mean(), 2)

    samsung_point = [round(sam_overall, 2), round(sam30['Point'].mean(), 2), round(sam31['Point'].mean(), 2),
                     round(sam32['Point'].mean(), 2), round(sam33['Point'].mean(), 2), round(sam34['Point'].mean(), 2)]

    xia30 = xiaomi.loc[(xiaomi['Week'] == 30)]
    xia31 = xiaomi.loc[(xiaomi['Week'] == 31)]
    xia32 = xiaomi.loc[(xiaomi['Week'] == 32)]
    xia33 = xiaomi.loc[(xiaomi['Week'] == 33)]
    xia34 = xiaomi.loc[(xiaomi['Week'] == 34)]

    round(xia30['Point'].mean(), 2)
    round(xia31['Point'].mean(), 2)
    round(xia32['Point'].mean(), 2)
    round(xia33['Point'].mean(), 2)
    round(xia34['Point'].mean(), 2)

    xiaomi_point = [round(xia_overall, 2), round(xia30['Point'].mean(), 2), round(xia31['Point'].mean(), 2),
                    round(xia32['Point'].mean(), 2), round(xia33['Point'].mean(), 2), round(xia34['Point'].mean(), 2)]

    real30 = realme.loc[(realme['Week'] == 30)]
    real31 = realme.loc[(realme['Week'] == 31)]
    real32 = realme.loc[(realme['Week'] == 32)]
    real33 = realme.loc[(realme['Week'] == 33)]
    real34 = realme.loc[(realme['Week'] == 34)]

    round(real30['Point'].mean(), 2)
    round(real31['Point'].mean(), 2)
    round(real32['Point'].mean(), 2)
    round(real33['Point'].mean(), 2)
    round(real34['Point'].mean(), 2)

    realme_point = [round(real_overall, 2), round(real30['Point'].mean(), 2), round(real31['Point'].mean(), 2),
                    round(real32['Point'].mean(), 2), round(real33['Point'].mean(), 2),
                    round(real34['Point'].mean(), 2)]

    other30 = others.loc[(others['Week'] == 30)]
    other31 = others.loc[(others['Week'] == 31)]
    other32 = others.loc[(others['Week'] == 32)]
    other33 = others.loc[(others['Week'] == 33)]
    other34 = others.loc[(others['Week'] == 34)]

    round(other30['Point'].mean(), 2)
    round(other31['Point'].mean(), 2)
    round(other32['Point'].mean(), 2)
    round(other33['Point'].mean(), 2)
    round(other34['Point'].mean(), 2)

    others_point = [round(other_overall, 2), round(other30['Point'].mean(), 2), round(other31['Point'].mean(), 2),
                    round(other32['Point'].mean(), 2), round(other33['Point'].mean(), 2),
                    round(other34['Point'].mean(), 2)
                    ]

    vivo30 = vivo.loc[(vivo['Week'] == 30)]
    vivo31 = vivo.loc[(vivo['Week'] == 31)]
    vivo32 = vivo.loc[(vivo['Week'] == 32)]
    vivo33 = vivo.loc[(vivo['Week'] == 33)]
    vivo34 = vivo.loc[(vivo['Week'] == 34)]

    round(vivo30['Point'].mean(), 2)
    round(vivo31['Point'].mean(), 2)
    round(vivo32['Point'].mean(), 2)
    round(vivo33['Point'].mean(), 2)
    round(vivo34['Point'].mean(), 2)

    vivo_point = [round(vivo_overall, 2), round(vivo30['Point'].mean(), 2), round(vivo31['Point'].mean(), 2),
                  round(vivo32['Point'].mean(), 2), round(vivo33['Point'].mean(), 2), round(vivo34['Point'].mean(), 2)]

    hua30 = huawei.loc[(huawei['Week'] == 30)]
    hua31 = huawei.loc[(huawei['Week'] == 31)]
    hua32 = huawei.loc[(huawei['Week'] == 32)]
    hua33 = huawei.loc[(huawei['Week'] == 33)]
    hua34 = huawei.loc[(huawei['Week'] == 34)]

    round(hua30['Point'].mean(), 2)
    round(hua31['Point'].mean(), 2)
    round(hua32['Point'].mean(), 2)
    round(hua33['Point'].mean(), 2)
    round(hua34['Point'].mean(), 2)

    huawei_point = [round(hua_overall, 2), round(hua30['Point'].mean(), 2), round(hua31['Point'].mean(), 2),
                    round(hua32['Point'].mean(), 2), round(hua33['Point'].mean(), 2), round(hua34['Point'].mean(), 2)]

    oppo30 = oppo.loc[(oppo['Week'] == 30)]
    oppo31 = oppo.loc[(oppo['Week'] == 31)]
    oppo32 = oppo.loc[(oppo['Week'] == 32)]
    oppo33 = oppo.loc[(oppo['Week'] == 33)]
    oppo34 = oppo.loc[(oppo['Week'] == 34)]

    round(oppo30['Point'].mean(), 2)
    round(oppo31['Point'].mean(), 2)
    round(oppo32['Point'].mean(), 2)
    round(oppo33['Point'].mean(), 2)
    round(oppo34['Point'].mean(), 2)

    oppo_point = [round(oppo_overall, 2), round(oppo30['Point'].mean(), 2), round(oppo31['Point'].mean(), 2),
                  round(oppo32['Point'].mean(), 2), round(oppo33['Point'].mean(), 2), round(oppo34['Point'].mean(), 2)]

    am_list = [samsung_point, xiaomi_point, oppo_point, vivo_point, realme_point, huawei_point, others_point]

    df_am = pd.DataFrame(am_list, columns=['Overall', '30Week', '31Week', '32Week', '33Week', '34Week'])

    df_prac = df_am
    df_prac['30Week'] = df_prac['30Week'] / df_prac['Overall']
    df_prac['31Week'] = df_prac['31Week'] / df_prac['Overall']
    df_prac['32Week'] = df_prac['32Week'] / df_prac['Overall']
    df_prac['33Week'] = df_prac['33Week'] / df_prac['Overall']
    df_prac['34Week'] = df_prac['34Week'] / df_prac['Overall']
    df_prac = df_prac[['Overall', '30Week', '31Week', '32Week', '33Week', '34Week']]

    del df_prac['Overall']

    # numpy list형식으로 Transpose
    segon = np.array(df_prac).T

    # #am_list 만든 순서로 column 명 설정
    segon_df = pd.DataFrame(segon, columns=['Samsung', 'Xiaomi', 'OPPO', 'Vivo', 'Realme', 'Huawei', 'Others'])

    # 벤더 별 갯수 및 묶인 순서 확인
    am_count = am['Vendor'].groupby(am['Vendor']).count()

    am_sort = am_count.sort_values(ascending=True)

    segon_df = segon_df[['Others', 'Huawei', 'Realme', 'Vivo', 'OPPO', 'Xiaomi', 'Samsung']]

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

    # list로 묶어서 출력한 뒤 df30_count, am그룹으로 묶은 갯수 결과 비교해보기
    df_list = [list(df30_count), list(df31_count), list(df32_count), list(df33_count), list(df34_count)]

    # 위에서 확인한 순서대로 vendor명 입력하여 column 재정렬
    df_vendor = pd.DataFrame(df_list, columns=['Huawei', 'OPPO', 'Others', 'Realme', 'Samsung', 'Vivo', 'Xiaomi'],
                             index=None)

    df_vendor = df_vendor[['Others', 'Huawei', 'Realme', 'Vivo', 'OPPO', 'Xiaomi', 'Samsung']]

    segon_df.to_csv("Amazon_5weeks_rating.csv")

    multiple = df_vendor * segon_df

    multiple.sum(axis=0)

    # 파이차트에 쓸 list임
    multiple_list = list(multiple.sum(axis=0))

    result = np.array(multiple).T

    result[0]

    # list 내의 vendor 순서별로 slicing해서 시각화 진행

    plt.rcParams['figure.figsize'] = [15, 9]
    group_names = ['Others', 'Huawei', 'Realme', 'Vivo', 'OPPO', 'Xiaomi', 'Samsung']
    group_size = multiple_list
    group_colors = ['#BAF1A1', '#76AD3B', '#FF9904', '#FDDB5E', 'green', '#F44E54', 'dodgerblue']
    # ['#F44E54', 'coral']
    group_explodes = (0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)

    plt.pie(group_size, explode=group_explodes, labels=group_names, colors=group_colors,
            autopct='%1.2f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Amazon Weighted Review Count Ratio 30 - 34 weeks', fontsize=20)
    plt.show()

    r = [0, 1, 2, 3, 4]
    raw_data = {'Samsung': result[6], \
                'Xiaomi': result[5], \
                'OPPO': result[4], \
                'Vivo': result[3], \
                'Realme': result[3], \
                'Huawei': result[2], \
                'Others': result[0]}

    df_stack = pd.DataFrame(raw_data)

    totals = [i + j + k + l + m + n + o for i, j, k, l, m, n, o in zip(df_stack['Xiaomi'],
                                                                       df_stack['Samsung'], df_stack['OPPO'],
                                                                       df_stack['Vivo'], df_stack['Realme'],
                                                                       df_stack['Huawei'], df_stack['Others'])]

    Samsung = [i / j * 100 for i, j in zip(df_stack['Samsung'], totals)]
    Xiaomi = [i / j * 100 for i, j in zip(df_stack['Xiaomi'], totals)]
    OPPO = [i / j * 100 for i, j in zip(df_stack['OPPO'], totals)]
    Vivo = [i / j * 100 for i, j in zip(df_stack['Vivo'], totals)]
    Realme = [i / j * 100 for i, j in zip(df_stack['Realme'], totals)]
    Huawei = [i / j * 100 for i, j in zip(df_stack['Huawei'], totals)]
    Others = [i / j * 100 for i, j in zip(df_stack['Others'], totals)]

    barWidth = 0.65
    names = ('30Week', '31Week', '32Week', '33Week', '34Week')

    # Create Bars
    plt.bar(r, Samsung, color='dodgerblue', edgecolor='white', width=barWidth,
            label="Samsung")

    plt.bar(r, Xiaomi, bottom=Samsung, color='#F44E54', edgecolor='white',
            width=barWidth, label="Xiaomi")

    plt.bar(r, OPPO, bottom=[i + j for i, j in zip(Samsung, Xiaomi)], color='green',
            edgecolor='white', width=barWidth, label="OPPO")

    plt.bar(r, Vivo, bottom=[i + j + k for i, j, k in zip(Samsung, Xiaomi, OPPO)],
            color='#FDDB5E', edgecolor='white', width=barWidth, label="Vivo")

    plt.bar(r, Realme, bottom=[i + j + k + l for i, j, k, l in zip(Samsung, Xiaomi, OPPO, Vivo)],
            color='#FF9904', edgecolor='white', width=barWidth, label="Realme")

    plt.bar(r, Huawei, bottom=[i + j + k + l + m for i, j, k, l, m in zip(Samsung, Xiaomi, OPPO, Vivo, Realme)],
            color='#76AD3B', edgecolor='white', width=barWidth, label="Huawei")

    plt.bar(r, Others,
            bottom=[i + j + k + l + m + n for i, j, k, l, m, n in zip(Samsung, Xiaomi, OPPO, Vivo, Realme, Huawei)],
            color='#BAF1A1', edgecolor='white', width=barWidth, label="Others")

    plt.title("Amazon Weighted 30 - 34 weeks Review Count", loc='left', fontsize=25, fontweight=0, color='black')

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
    y = [result[6], result[5], result[4], result[3], result[2], result[1], result[0]]  # Reivew 갯수 누적

    pal = ['dodgerblue', '#F44E54', 'green', '#FDDB5E', '#FF9904', '#76AD3B', '#BAF1A1']
    # pal = ["#A20101", "#F44E54", "#FF9904", "#FDDB5E", "#BAF1A1", "#76AD3B", "#0A709A"]
    plt.stackplot(x, y, labels=['Samsung', 'Xiaomi', 'OPPO', 'Vivo', 'Realme', 'Huawei', 'Others'],
                  colors=pal, alpha=0.45)

    plt.title("Amazon Weighted 30 - 34 weeks Review Count", loc='left', fontsize=25, fontweight=0, color='black')
    plt.xlabel("Weeks", fontsize=17)
    plt.xticks(fontsize=15)

    plt.ylabel("Review counts", fontsize=17)
    plt.yticks(fontsize=15)

    plt.legend(loc='upper right', fontsize=15)
    plt.rcParams['figure.figsize'] = [15, 9]
    plt.show()