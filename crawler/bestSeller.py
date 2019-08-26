from crawler.crawler import *


def get_bestSeller():
    # 아마존 베스트셀러 링크 연결
    urls = get_amazon_link()
    browser, url_header = get_browser_options()
    try:
        links = []
        listName = 'zg-ordered-list'
        for url in urls:
            browser.get(url)
            WebDriverWait(browser, 100).until(
                EC.presence_of_element_located((By.ID, listName))
            )
            page = browser.page_source
            soup = BeautifulSoup(page, 'html.parser')
            rank = soup.find("ol", id=listName)
            # print(rank)

            product_list = soup.select('a[class=a-link-normal]')
            # print(product_list)

            for link in product_list:
                if 'href' in link.attrs:
                    if link.attrs['href'][0] != 'h' and "/product-reviews/" not in link.attrs['href']:
                        # print(link.attrs['href'])
                        links.append(link.attrs['href'])

            # print(product_list[0]['href'])

        # 오늘 날짜에 저장하기
        filepath = "./" + get_current_date() + "/bestseller_link.txt"
        with open(filepath, 'w') as f:
            for idx, item in enumerate(links):
                f.write('{}\t{}\n'.format(idx + 1, item))

    finally:
        browser.quit()
