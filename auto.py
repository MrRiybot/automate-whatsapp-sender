from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import itertools
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="chromedriver.exe")
wait = WebDriverWait(driver, 60)
print("Chrome opened successfully!")

Web_whatsapp = 'https://web.whatsapp.com/'  # scan the code
driver.get(Web_whatsapp)
input("Accessing Whatsapp web, please scan the qr code!, If you are done press ENTER")

df = pd.read_csv("numbers.csv")
names = df['Name'].dropna().tolist()
numbers = df['Number'].dropna().tolist()
names = names[1:]
numbers = numbers[1:]

with open('msg.txt', 'r',encoding='utf8') as file:
    data = file.read().replace('\n', '%0A')

for i, j in zip(numbers, names):
    web_page = driver.get("https://web.whatsapp.com/send?phone=+{}&text={}&app_absent=1".format(str(i).replace('{NAME}',str(j) ), data))
    time.sleep(20)
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]/button')
    button.click()
    time.sleep(5)
driver.close()
