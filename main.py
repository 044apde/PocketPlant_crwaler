from re import S
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from tqdm import tqdm
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


listOfName = []
url = 'https://www.xplant.co.kr/shop/list.php?ca_id=10'


def setChromeDriver():  # First
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


def openChrome():
    driver.get(url)
    driver.implicitly_wait(10)


def getNameOfPlant():
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    order = 1
    try:
        for i in range(1, 100):
            name = soup.select_one(
                '#search_area > div.search_item_area > div:nth-child(' + str(i) + ') > div > div > p.textEllipsis > a > b')
            if name != None:
                listOfName.append(name.get_text())
    except:
        print('ERROR: getNameOfPlant')


def moveNextPage(count):
    driver.find_element(
        By.CSS_SELECTOR, '#search_area > div.search_paging_area > table > tbody > tr > td > font + a').click()
    time.sleep(3)


def startCrwaling():
    print('Starting..')
    openChrome()
    for repeat in range(1, 5):
        getNameOfPlant()
        moveNextPage(repeat)
    print('Finshed.')


# Start Here
driver = setChromeDriver()
startCrwaling()
