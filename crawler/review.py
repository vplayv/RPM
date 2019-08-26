from crawler.crawler import *


def get_information():
    filename = "./" + get_current_date() + "/information.csv"
    file = pd.read_csv(filename)

    pd.set_option("display.max_rows", 101)
    pd.set_option("display.max_columns", 13)

    # print(file, file.shape)
    file = file.drop_duplicates(["Num_reviews"], keep="first", inplace=False)
    # print(file, file.shape)
    # file['Product_name'] = file['Product_name'].map(lambda x: x.rstrip('('))
    sep = '('
    file['Product_name'] = file['Product_name'].str.split(sep, 1).str.get(0)
    file['Product_name'] = file['Product_name'].str.rstrip()
    file = file.drop_duplicates(["Product_name"], keep="first", inplace=False)
    # print(file, file.shape)
    # print(file[["Product_name", "LINK"]].to_numpy())
    return file[["Product_name", "LINK"]].to_numpy()


def get_reivew_count(myList):
    length = len(myList)
    string = ""
    for idx in range(2, length):
        string = string + myList[idx]

    return int(string)


def get_content(link, date):
    # DataFrame
    lock = Lock()
    select_option = 1  # 0이면 Top rated 1이면 Most Recent
    name = link[0]
    link = link[1]
    start_date, end_date = date
    browser, url_header = get_browser_options()

    # print(name, link)
    # print(start_date, end_date)

    try:
        print(name, link)

        while True:
            try:
                if validators.url(link) == False:
                    return
                browser.get(link)
                driver_wait(browser, 60, By.ID, "centerCol")
            except TimeoutException:
                print("Timeout, retrying...")
                continue
            except Exception as e:
                print("Dont Know Error : " + e)
                if link is not None:
                    print("ERROR LINK : " + link)
                return
            else:
                break

        page = browser.page_source
        soup = BeautifulSoup(page, 'html.parser')
        filename = "./" + get_current_date() + "/reviews.csv"

        loc_count = 0
        review_links = []
        if soup.find("a", class_="a-size-base a-link-normal 1star") is not None:
            review_links.append(soup.find("a", class_="a-size-base a-link-normal 1star")['href'])

        if soup.find("a", class_="a-size-base a-link-normal 2star") is not None:
            review_links.append(soup.find("a", class_="a-size-base a-link-normal 2star")['href'])

        if soup.find("a", class_="a-size-base a-link-normal 3star") is not None:
            review_links.append(soup.find("a", class_="a-size-base a-link-normal 3star")['href'])

        if soup.find("a", class_="a-size-base a-link-normal 4star") is not None:
            review_links.append(soup.find("a", class_="a-size-base a-link-normal 4star")['href'])

        if soup.find("a", class_="a-size-base a-link-normal 5star") is not None:
            review_links.append(soup.find("a", class_="a-size-base a-link-normal 5star")['href'])

        review_bodys = []
        # 점수별 for문
        for idx2, review_link in enumerate(review_links):
            # print("review {}".format(idx2 + 1))

            # Link 얻어오기
            review_link = url_header + review_link
            browser.get(review_link)

            # wait
            driver_wait(browser, 60, By.ID, "reviews-container")

            # Most recent 선택
            select_element = Select(browser.find_element_by_css_selector("#sort-order-dropdown"))
            select_element.select_by_index(select_option)
            driver_wait(browser, 60, By.CSS_SELECTOR, "#sort-order-dropdown > option:nth-child(2)")
            browser.refresh()

            # wait
            driver_wait(browser, 60, By.ID, "reviews-container")

            page = browser.page_source
            soup = BeautifulSoup(page, 'html.parser')
            tmp = soup.find("span", {"data-hook": "cr-filter-info-review-count"}).getText()
            numbers = re.findall("\d+", tmp)
            number = get_reivew_count(numbers)
            review_count = min(500, int((number - 1) / 10))
            print(review_count)

            df_colums = ["Product_name", "Title", "Point", "Date", "Vote", "Review"]
            df = pd.DataFrame(columns=df_colums)

            for idx3 in range(review_count):
                driver_wait(browser, 60, By.ID, "cm_cr-review_list")
                driver_wait(browser, 60, By.CSS_SELECTOR, "#sort-order-dropdown > option:nth-child(2)")

                page = browser.page_source
                soup = BeautifulSoup(page, 'html.parser')
                review_data = soup.find_all("div", class_="a-section review aok-relative")
                # print(len(review_data))

                date_check = datetime.time

                for idx4 in range(len(review_data)):

                    review_date = review_data[idx4].find("span", {"data-hook": "review-date"})
                    if review_date is not None:
                        review_date = review_data[idx4].find("span", {"data-hook": "review-date"}).getText()
                        review_date = datetime.datetime.strptime(review_date, '%d %B %Y').date()

                    date_check = review_date

                    review_title = review_data[idx4].find("a", {"data-hook": "review-title"})
                    if review_title is not None:
                        review_title = review_data[idx4].find("a", {"data-hook": "review-title"}).getText()

                    review_point = review_data[idx4].find("span", class_="a-icon-alt")
                    if review_point is not None:
                        review_point = review_data[idx4].find("span", class_="a-icon-alt").getText()


                    # review_feature = review_data[idx4].find("a", {"data-hook": "format-strip"})
                    # if review_feature is not None:
                    #     review_feature = review_data[idx4].find("a", {"data-hook": "format-strip"}).getText()

                    review_body = review_data[idx4].find("span",
                                                         class_="a-size-base review-text review-text-content")
                    if review_body is not None:
                        review_body = review_data[idx4].find("span",
                                                             class_="a-size-base review-text review-text-content").getText()
                    # 전처리
                    review_point = review_point[:3]
                    pattern = '([0-9]+:[0-9]+:[0-9]+This video is not intended for all audiences.[a-zA-z0-9-\?\s\.]+Install Flash Player)+'
                    repl = ''
                    review_body = re.sub(pattern=pattern, repl=repl, string=review_body)
                    review_body = review_body.replace('\n', ' ')
                    review_bodys.append(review_body)

                    review_recommand = review_data[idx4].find("span",
                                                              class_="a-size-base a-color-tertiary cr-vote-text")

                    if review_recommand is not None:
                        review_recommand = review_data[idx4].find("span",
                                                                  class_="a-size-base a-color-tertiary cr-vote-text").getText()
                        # print(review_recommand.split()[0])
                        if review_recommand.split()[0] == "One":
                            review_recommand = 1
                        else:
                            review_recommand = review_recommand.split()[0]
                    else:
                        review_recommand = 0

                    # print(review_title)
                    # print(review_point)
                    # print(review_date)
                    # print(review_feature)
                    # print(review_body)
                    # print(review_recommand)

                    df.loc[loc_count] = [name, review_title, review_point, review_date, review_recommand, review_body]
                    # df.loc[loc_count] = [review_title, review_point, review_date, review_feature, review_body]
                    loc_count = loc_count + 1

                if soup.find("li", class_="a-last") is None:
                    break

                if start_date > date_check:
                    # print(start_date, )
                    break

                next_page = soup.find("li", class_="a-last").find("a")['href']
                next_page = url_header + next_page
                # print(next_page)
                browser.get(next_page)

            # Save
            lock.acquire()
            df.to_csv(filename, mode='a', index=False, header=False, encoding='utf-8')
            lock.release()
            print(name + " save")
    except Exception as e:
        print(e)

    finally:
        browser.quit()
        print(name + " end")


def review(date):
    links = get_information()
    print(len(links))

    df_colums = ["Product_name", "Title", "Point", "Date", "Vote", "Review"]
    df = pd.DataFrame(columns=df_colums)

    filename = "./" + get_current_date() + "/reviews.csv"
    # print(filename)
    df.to_csv(filename, mode='w', index=False, encoding='utf-8')

    # n-1 개의 프로세스를 사용합니다.
    cpu_count = multiprocessing.cpu_count()
    # cpu_count = 2
    pool = Pool(processes=(cpu_count - 1))

    pool.starmap(get_content, zip(links, repeat(date)))
