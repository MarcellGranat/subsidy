from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Runs Chrome in headless mode.
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")

url = "https://www.palyazat.gov.hu/tamogatott_projektkereso"
print(url)

subsidy_types = ['Széchenyi Terv Plusz', 'Széchenyi 2020', 'KTIA',
                 'Széchenyi 2020 Pénzügyi Eszközök', 'NFT', 'EU 2007-2013', 'Széchenyi 2020 VP']

driver = webdriver.Chrome(
    chrome_options=options, executable_path='C:/Users/Marci/Downloads/chromedriver_win32/chromedriver.exe')
# driver = webdriver.Chrome(
#    executable_path='C:/Users/Marci/Downloads/chromedriver_win32/chromedriver.exe')

for subsidy_type in subsidy_types:
    print(subsidy_type)
    driver.get(url)
    time.sleep(2)
    subsidy_type_field = driver.find_element_by_css_selector(
        '#root > .container , #programok .css-1hwfws3')
    subsidy_type_field.send_keys('Széchenyi Terv Plusz')
    time.sleep(2)

driver.close()
