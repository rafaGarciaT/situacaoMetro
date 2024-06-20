import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()), options=chrome_options)

url = "https://www.diretodostrens.com.br/?codigo=2"
headers = {
    "User-Agent": "situacaoMetro/1.0 (+https://github.com/rafaelGarcia1oACienciaDaComputacao/situacaoMetro)"
}

driver.get(url)
page_source = driver.page_source
time.sleep(5)
driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')
print(soup.title)

table = soup.find("table", class_="table table-hover")
tbody = table.find("tbody")

for tr in tbody.find_all('tr'):
    print("tr " + str(tr) + " tr")
    tds = tr.find_all('td')
    if len(tds) >= 3:
        td1_text = tds[0].find('a')
        td2_text = tds[1].get_text(strip=True)
        td3_text = tds[2].get_text(strip=True)
        print(f'TD1: {td1_text.get_text(strip=True)}, TD2: {td2_text}, TD3: {td3_text}')
