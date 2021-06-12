from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path = './venv/Lib/chromedriver.exe')

list_url = [
    'https://dailybonnet.com/',
    'https://thehardtimes.net/',
    'https://www.thebeaverton.com/',
    'https://www.thepoke.co.uk/',
    'https://newsthump.com/',
    'http://www.newsbiscuit.com/'
]

filename = "satirical.csv"
month = 5
year = 2021

while(year > 2018):
    url_new = list_url[0] + str(year) + '/' + str(month)
    print(url_new)

    browser.get(url_new)

    num_page = 1

    while True:
        sleep(3)

        title_list = browser.find_elements_by_xpath("//a[@rel='bookmark']")

        with open(filename, 'a') as csvfile:
            for title in title_list:
                title = title.text.replace(',', '(comma)')
                title = title + ', 1'
                csvfile.write(title)
                csvfile.write('\n')

        print('done page : ', num_page)
        num_page += 1

        try:
            next_page = browser.find_element_by_xpath("//a[@class='next page-numbers']")
            next_page.click()
        except:
            print('DONE LINK')
            break
    month -= 1
    if month == 0:
        month = 12
        year -= 1

month = 5
year = 2021
while(year > 2018):
    url_new = list_url[1] + str(year) + '/' + str(month)
    print(url_new)

    browser.get(url_new)

    num_page = 1

    while True:
        sleep(3)

        title_list = browser.find_elements_by_xpath("//h2[@class='post-title']")

        with open(filename, 'a', encoding="utf-8") as csvfile:
            for title in title_list:
                title = title.text.replace(',', '(comma)')
                title = title + ', 1'
                csvfile.write(title)
                csvfile.write('\n')

        print('done page : ', num_page)
        num_page += 1

        try:
            next_page = browser.find_element_by_xpath("//a[@class='next page-numbers']")
            next_page.click()
        except:
            print('DONE LINK')
            break
    month -= 1
    if month == 0:
        month = 12
        year -= 1

month = 5
year = 2021
while(year > 2018):
    url_new = list_url[2] + str(year) + '/' + str(month)
    print(url_new)

    browser.get(url_new)

    num_page = 1

    while True:
        sleep(3)

        title_list = browser.find_elements_by_xpath("//h3[@itemprop='headline']")

        with open(filename, 'a', encoding="utf-8") as csvfile:
            for title in title_list:
                title = title.text.replace(',', '(comma)')
                title = title + ', 1'
                csvfile.write(title)
                csvfile.write('\n')

        print('done page : ', num_page)
        num_page += 1

        try:
            next_page = browser.find_element_by_xpath("//i[@class='fa fa-angle-left']")
            next_page.click()
        except:
            print('DONE LINK')
            break
    month -= 1
    if month == 0:
        month = 12
        year -= 1

month = 5
year = 2021
while(year > 2018):
    url_new = list_url[3] + str(year) + '/' + str(month)
    print(url_new)

    browser.get(url_new)

    num_page = 1

    while True:
        sleep(3)

        title_list = browser.find_elements_by_xpath("//div[@class='txt']")

        with open(filename, 'a', encoding="utf-8") as csvfile:
            for title in title_list:
                title = title.text.replace(',', '(comma)')
                title = title.split('\n')[1]
                title = title + ', 1'
                csvfile.write(title)
                csvfile.write('\n')

        print('done page : ', num_page)
        num_page += 1

        try:
            next_page = browser.find_element_by_xpath("//div[@class='prev']")
            next_page.click()
        except:
            print('DONE LINK')
            break
    month -= 1
    if month == 0:
        month = 12
        year -= 1

month = 5
year = 2021
while(year > 2018):
    url_new = list_url[4] + str(year) + '/' + str(month)
    print(url_new)

    browser.get(url_new)

    num_page = 1

    sleep(3)
    title_list = browser.find_elements_by_xpath("//a[@rel='bookmark']")

    with open(filename, 'a', encoding = "utf-8") as csvfile:
        for title in title_list:
            title = title.text.replace(',', '(comma)')
            title = title + ', 1'
            csvfile.write(title)
            csvfile.write('\n')

    print('done page : ', num_page)
    num_page += 1

    try:
        next_page = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[7]/p/a")
        next_page.click()
    except:
        print('DONE LINK')
        break

    while True:
        sleep(3)

        title_list = browser.find_elements_by_xpath("//a[@rel='bookmark']")

        with open(filename, 'a', encoding="utf-8") as csvfile:
            for title in title_list:
                title = title.text.replace(',', '(comma)')
                title = title + ', 1'
                csvfile.write(title)
                csvfile.write('\n')

        print('done page : ', num_page)
        num_page += 1

        try:
            next_page = browser.find_element_by_xpath("//p[@class='previous floated']")
            next_page.click()
        except:
            print('DONE LINK')
            break
    month -= 1
    if month == 0:
        month = 12
        year -= 1

month = 5
year = 2021
while(year > 2018):
    url_new = list_url[5] + str(year) + '/' + str(month)
    print(url_new)

    browser.get(url_new)

    num_page = 1

    sleep(3)

    title_list = browser.find_elements_by_xpath("//div[@class='col-sm-8 text-center']/h3")

    with open(filename, 'a', encoding = "utf-8") as csvfile:
        for title in title_list:
            title = title.text.replace(',', '(comma)')
            title = title + ', 1'
            csvfile.write(title)
            csvfile.write('\n')

    print('done page : ', num_page)
    num_page += 1

    while True:
        url_new_2 = url_new + "/page/" + str(num_page)

        browser.get(url_new_2)

        sleep(3)

        title_list = browser.find_elements_by_xpath("//div[@class='col-sm-8 text-center']/h3")

        if len(title_list) == 0:
            print('DONE LINK')
            break

        with open(filename, 'a', encoding="utf-8") as csvfile:
            for title in title_list:
                title = title.text.replace(',', '(comma)')
                title = title + ', 1'
                csvfile.write(title)
                csvfile.write('\n')

        print('done page : ', num_page)
        num_page += 1

    month -= 1
    if month == 0:
        month = 12
        year -= 1
browser.close()
