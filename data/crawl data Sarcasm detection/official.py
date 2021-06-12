from selenium import webdriver
from time import sleep
import datetime

browser = webdriver.Chrome(executable_path = './venv/Lib/chromedriver.exe')

list_url = [
    'https://www.euronews.com/',
    'https://www.france24.com/en/archives/2021/06/06-June-2021',
    'https://www.france24.com/en/archives/2020/12/31-December-2020',
    'https://www.france24.com/en/archives/2019/12/31-December-2019',
    'https://www.canindia.com/category/world/',
    'https://www.canindia.com/category/entertainment/',
    'https://www.canindia.com/category/sports/',
    'https://www.canindia.com/category/business-economy/',
    'https://www.canindia.com/category/health/',
    'https://www.canindia.com/category/cricket-2/',
    'https://www.canindia.com/category/bollywood/',
    'https://www.canindia.com/category/fashion/',
    'https://www.canindia.com/category/south-asia/',
    'https://www.canindia.com/category/lifestyle/',
]

filename = "official.csv"

x = datetime.datetime(2021, 6, 10)
day = x.day
month = x.month
year = x.year

while(year > 2018):
    if day >= 10:
        url_new = list_url[0] + str(year) + '/' + str(month) + '/' + str(day)
    else:
        url_new = list_url[0] + str(year) + '/' + str(month) + '/0' + str(day)

    print(url_new)

    browser.get(url_new)

    sleep(3)

    title_list = browser.find_elements_by_xpath("//a[@rel='bookmark']")

    with open(filename, 'a', encoding = "utf-8") as csvfile:
        for title in title_list:
            title = title.text.replace(',', '(comma)')
            title = title + ', 0'
            csvfile.write(title)
            csvfile.write('\n')


    print('done : ', day, '/', month, '/', year)

    x -= datetime.timedelta(days = 1)
    day = x.day
    month = x.month
    year = x.year

for url in list_url[1:4]:
    print(url)

    browser.get(url)

    num_page = 1

    while(1):
        sleep(3)

        title_list = browser.find_elements_by_xpath("//a[@class='a-archive-link']")

        with open(filename, 'a', encoding="utf-8") as csvfile:
            for title in title_list:
                title = title.text.replace(',', '(comma)')
                title = title + ', 0'
                csvfile.write(title)
                csvfile.write('\n')

        print('done page : ', num_page)
        num_page += 1

        try:
            next_page = browser.find_element_by_xpath("//a[@class='o-archive-day__nav__link']")
            next_page.click()
        except:
            print('DONE LINK')
            break

list_num_page = [1587, 1257, 1132, 1058, 801, 720, 627, 368, 330, 294]

for url in list_url[4:]:

    num_page = 1

    for num in list_num_page:
        while(num_page <= num):
            url_new = url + 'page/' + str(num_page)

            print(url_new)
            browser.get(url_new)
            sleep(3)

            title_list = browser.find_elements_by_xpath("//a[@rel='bookmark']")

            with open(filename, 'a', encoding="utf-8") as csvfile:
                for title in title_list:
                    title = title.text.replace(',', '(comma)')
                    if len(title) == 0:
                        continue
                    title = title + ', 0'
                    csvfile.write(title)
                    csvfile.write('\n')

            print('done page : ', num_page)
            num_page += 1

        print('DONE LINK')

browser.close()
