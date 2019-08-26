from crawler.crawler import *


def By_price(soup, className):
    price = soup.find("span", class_=className)
    if price is not None:
        price = price.getText()
    else:
        price = soup.find("span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
        if price is not None:
            price = price.getText()
        else:
            price = soup.find("span", class_="olp-padding-right")
            if price is not None:
                price = soup.find("span", class_="olp-padding-right").find("span", class_="a-color-price")
                price = price.getText()

    if price is not None:
        price = price.strip('₹ ')
        price = price.strip()

    # print(price)
    return price


def By_star(soup, className):
    star = soup.find("a",
                     class_=className)

    if star is not None:
        star = star.getText()
        # print(star)
    else:
        star = "0%"

    return star


def By_feature(soup, _id):
    feature = soup.find("div", id=_id)
    if feature is not None:
        feature = soup.find("div", id=_id).find("span", class_="a-size-base a-color-tertiary")
        feature = feature.getText()
        # print(feature)

    return feature

def get_content(link):
    # DataFrame
    lock = Lock()

    rank = link[0]
    link = link[1]
    browser, url_header = get_browser_options()
    link = url_header + link

    df_colums = ["Rank", "Vendor", "Product_name", "Ratings", "Num_reviews", "Five_star", "Four_star",
                 "Three_star", "Two_star", "One_star", "MRP", "DP", "Battery_life", "Fingerprint_reader",
                 "Camera_quality", "Sound_quality", "Face_recognition", "Image_stabilization", "Value_for_money",
                 "For_gaming", "Screen_quality", "Low_light", "Material_quality", "Electronics Rank", "SmartPhone Rank",
                 "First_Available", "LINK"]

    df = pd.DataFrame(columns=df_colums)

    try:
        while True:
            try:
                browser.get(link)
                WebDriverWait(browser, 30).until(
                    EC.presence_of_element_located((By.ID, "centerCol"))
                )
            except TimeoutException:
                print("Timeout, retrying...")
                continue
            else:
                break

        page = browser.page_source
        soup = BeautifulSoup(page, 'html.parser')
        # print(soup.prettify())

        Rank = str(rank)

        # 제조사
        Vendor = soup.find("a", id="bylineInfo")
        Vendor = Vendor.getText().strip()
        # print(Vendor)

        # 제품명
        Product_name = soup.find("span", id="productTitle")
        Product_name = Product_name.getText().strip()
        # print(Product_name)

        # 평점
        acrPopover = soup.find("span", id="acrPopover")
        if acrPopover is not None:
            acrPopover = acrPopover['title']
            acrPopover = acrPopover[:3]
            # print(acrPopover)

        # 리뷰 수
        total_reivew_count = soup.find("span", id="acrCustomerReviewText")

        if total_reivew_count is not None:
            total_reivew_count = total_reivew_count.getText()
            total_reivew_count = total_reivew_count.replace(" customer reviews", "")
            total_reivew_count = total_reivew_count.replace(" customer review", "")
            # print(total_reivew_count)

        # 평점 비율
        five_star = By_star(soup, "a-size-base a-link-normal 5star histogram-review-count a-color-secondary")
        four_star = By_star(soup, "a-size-base a-link-normal 4star histogram-review-count a-color-secondary")
        three_star = By_star(soup, "a-size-base a-link-normal 3star histogram-review-count a-color-secondary")
        two_star = By_star(soup, "a-size-base a-link-normal 2star histogram-review-count a-color-secondary")
        one_star = By_star(soup, "a-size-base a-link-normal 1star histogram-review-count a-color-secondary")

        # 출고가
        MRP = By_price(soup, "priceBlockStrikePriceString a-text-strike")

        # 판매가
        deal_price = By_price(soup, "a-size-medium a-color-price priceBlockDealPriceString")

        # 특징
        Battery_life = By_feature(soup, "cr-summarization-attribute-attr-battery-life")
        Fingerprint_reader = By_feature(soup, "cr-summarization-attribute-attr-fingerprint-reader")
        Camera_quality = By_feature(soup, "cr-summarization-attribute-attr-camera-quality")
        Sound_quality = By_feature(soup, "cr-summarization-attribute-attr-sound-quality")
        Face_recognition = By_feature(soup, "cr-summarization-attribute-attr-face-recognition")
        Image_stabilization = By_feature(soup, "cr-summarization-attribute-attr-image-stabilization")
        Value_for_money = By_feature(soup, "cr-summarization-attribute-attr-value")
        For_gaming = By_feature(soup, "cr-summarization-attribute-attr-for-gaming")
        Screen_quality = By_feature(soup, "cr-summarization-attribute-attr-screen-display")
        Low_light = By_feature(soup, "cr-summarization-attribute-attr-for-low-light")
        Material_quality = By_feature(soup, "cr-summarization-attribute-attr-material-quality")

        # Electronics Rank
        Electronics_Rank = soup.find("tr", id="SalesRank")
        if Electronics_Rank is not None:
            Electronics_Rank = Electronics_Rank.find("td", class_="value").getText().split()[0].replace('#', '')
            # print(Electronics_Rank)

        # SmartPhone Rank
        SmartPhone_Rank = soup.find("ul", class_="zg_hrsr")
        if SmartPhone_Rank is not None:
            SmartPhone_Rank = SmartPhone_Rank.find("span", class_="zg_hrsr_rank").getText().strip().replace('#', '')
            # print(SmartPhone_Rank)

        # Date First Available
        First_Available = soup.find("tr", class_="date-first-available")
        if First_Available is not None:
            First_Available = First_Available.find("td", class_="value").getText()
            # print(First_Available.getText())

        # 행 추가
        df.loc[0] = [Rank, Vendor, Product_name, acrPopover, total_reivew_count,
                     five_star, four_star, three_star, two_star, one_star, MRP, deal_price,
                     Battery_life, Fingerprint_reader, Camera_quality, Sound_quality, Face_recognition,
                     Image_stabilization, Value_for_money, For_gaming, Screen_quality, Low_light, Material_quality,
                     Electronics_Rank, SmartPhone_Rank, First_Available, link]
        # print(
        #     Rank + " " + Vendor + " " + Product_name + " " + acrPopover + " " + total_reivew_count + "  " + five_star +
        #     " " + four_star + " " + three_star + " " + two_star + " " + one_star + " " + MRP + " " + deal_price)

    finally:
        browser.quit()
        filename = "./" + get_current_date() + "/information.csv"

        lock.acquire()
        df.to_csv(filename, mode='a', index=False, header=False, encoding='utf-8')
        lock.release()
        print(rank + " end")

def get_content_single(links):

    browser, url_header = get_browser_options()
    df_colums = ["Rank", "Vendor", "Product_name", "Ratings", "Num_reviews", "Five_star", "Four_star",
                 "Three_star", "Two_star", "One_star", "MRP", "DP", "Battery_life", "Fingerprint_reader",
                 "Camera_quality", "Sound_quality", "Face_recognition", "Image_stabilization", "Value_for_money",
                 "For_gaming", "Screen_quality", "Low_light", "Material_quality", "Electronics Rank", "SmartPhone Rank",
                 "First_Available", "LINK"]

    df = pd.DataFrame(columns=df_colums)
    filename = "./" + get_current_date() + "/information.csv"
    try:
        for idx, link in enumerate(links):
            # print("#{}".format(idx + 1))
            # BestSeller Rank
            Rank = link[0]
            link = link[1]
            link = url_header + link

            while True:
                try:
                    browser.get(link)
                    WebDriverWait(browser, 30).until(
                        EC.presence_of_element_located((By.ID, "centerCol"))
                    )
                except TimeoutException:
                    print("Timeout, retrying...")
                    continue
                except Exception as e:
                    print("Dont Know Error : " + e)
                    return
                else:
                    break

            page = browser.page_source
            soup = BeautifulSoup(page, 'html.parser')
            # print(soup.prettify())

            # 제조사
            Vendor = soup.find("a", id="bylineInfo")
            Vendor = Vendor.getText().strip()
            # print(Vendor)

            # 제품명
            Product_name = soup.find("span", id="productTitle")
            Product_name = Product_name.getText().strip()
            # print(Product_name)

            # 평점
            acrPopover = soup.find("span", id="acrPopover")
            if acrPopover is not None:
                acrPopover = acrPopover['title']
                acrPopover = acrPopover[:3]
                # print(acrPopover)

            # 리뷰 수
            total_reivew_count = soup.find("span", id="acrCustomerReviewText")

            if total_reivew_count is not None:
                total_reivew_count = total_reivew_count.getText()
                total_reivew_count = total_reivew_count.replace(" customer reviews", "")
                total_reivew_count = total_reivew_count.replace(" customer review", "")
                # print(total_reivew_count)

            # 평점 비율
            five_star = By_star(soup, "a-size-base a-link-normal 5star histogram-review-count a-color-secondary")
            four_star = By_star(soup, "a-size-base a-link-normal 4star histogram-review-count a-color-secondary")
            three_star = By_star(soup, "a-size-base a-link-normal 3star histogram-review-count a-color-secondary")
            two_star = By_star(soup, "a-size-base a-link-normal 2star histogram-review-count a-color-secondary")
            one_star = By_star(soup, "a-size-base a-link-normal 1star histogram-review-count a-color-secondary")

            # 출고가
            MRP = By_price(soup, "priceBlockStrikePriceString a-text-strike")

            # 판매가
            deal_price = By_price(soup, "a-size-medium a-color-price priceBlockDealPriceString")

            # 특징
            Battery_life = By_feature(soup, "cr-summarization-attribute-attr-battery-life")
            Fingerprint_reader = By_feature(soup, "cr-summarization-attribute-attr-fingerprint-reader")
            Camera_quality = By_feature(soup, "cr-summarization-attribute-attr-camera-quality")
            Sound_quality = By_feature(soup, "cr-summarization-attribute-attr-sound-quality")
            Face_recognition = By_feature(soup, "cr-summarization-attribute-attr-face-recognition")
            Image_stabilization = By_feature(soup, "cr-summarization-attribute-attr-image-stabilization")
            Value_for_money = By_feature(soup, "cr-summarization-attribute-attr-value")
            For_gaming = By_feature(soup, "cr-summarization-attribute-attr-for-gaming")
            Screen_quality = By_feature(soup, "cr-summarization-attribute-attr-screen-display")
            Low_light = By_feature(soup, "cr-summarization-attribute-attr-for-low-light")
            Material_quality = By_feature(soup, "cr-summarization-attribute-attr-material-quality")

            # Electronics Rank
            Electronics_Rank = soup.find("tr", id="SalesRank")
            if Electronics_Rank is not None:
                Electronics_Rank = Electronics_Rank.find("td", class_="value").getText().split()[0].replace('#', '')
                # print(Electronics_Rank)

            # SmartPhone Rank
            SmartPhone_Rank = soup.find("ul", class_="zg_hrsr")
            if SmartPhone_Rank is not None:
                SmartPhone_Rank = SmartPhone_Rank.find("span", class_="zg_hrsr_rank").getText().strip().replace('#', '')
                # print(SmartPhone_Rank)

            # Date First Available
            First_Available = soup.find("tr", class_="date-first-available")
            if First_Available is not None:
                First_Available = First_Available.find("td", class_= "value").getText()
                # print(First_Available.getText())



            # 행 추가
            df.loc[0] = [Rank, Vendor, Product_name, acrPopover, total_reivew_count,
                         five_star, four_star, three_star, two_star, one_star, MRP, deal_price,
                         Battery_life, Fingerprint_reader, Camera_quality, Sound_quality, Face_recognition,
                         Image_stabilization, Value_for_money, For_gaming, Screen_quality, Low_light, Material_quality,
                         Electronics_Rank, SmartPhone_Rank, First_Available, link]

            df.to_csv(filename, mode='a', index=False, header=False, encoding='utf-8')

    finally:
        browser.quit()


def information(information_option):
    links = []
    df_colums = ["Rank", "Vendor", "Product_name", "Ratings", "Num_reviews", "Five_star", "Four_star",
                 "Three_star", "Two_star", "One_star", "MRP", "DP", "Battery_life", "Fingerprint_reader",
                 "Camera_quality", "Sound_quality", "Face_recognition", "Image_stabilization", "Value_for_money",
                 "For_gaming", "Screen_quality", "Low_light", "Material_quality", "Electronics Rank", "SmartPhone Rank",
                 "First_Available", "LINK"]
    # 오늘 날짜 링크 열기
    bestseller_link = "./" + get_current_date() + "/bestseller_link.txt"
    with open(bestseller_link, 'r') as f:
        links = f.readlines()
    f.close()

    links = [link.rstrip('\n') for link in links]
    links = [link.split('\t') for link in links]
    links = np.array(links)

    df = pd.DataFrame(columns=df_colums)

    filename = "./" + get_current_date() + "/information.csv"
    # print(filename)
    df.to_csv(filename, mode='w', index=False, encoding='utf-8')
    if information_option == 1:
        print("single cpu")
        get_content_single(links)

    elif information_option == 2:
        print("multi processing cpu")
        cpu_count = multiprocessing.cpu_count()
        pool = Pool(processes=(cpu_count - 1))
        pool.map(get_content, links)

