from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(START_URL)

scraped_data = []

def scrape():
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    bright_star_table = soup.find("table", {'class': 'wikitable'})
    table_rows = bright_star_table.find_all("tr")
    for row in table_rows:
        cols = row.find_all('td')
        temp_list = []
        for col_data in cols:
            data = col_data.text.strip()
            temp_list.append(data)
        if(len(temp_list)>0):
            scraped_data.append(temp_list)



scrape()
print(scraped_data)

stars_data = []
for i in range(0, len(scraped_data)):
    Star_name = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]
    required_data = [Star_name, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

headers = ['name', 'dist', 'mass', 'rad', 'lum']
stars_data_1 = pd.DataFrame(stars_data, columns=headers)
stars_data_1.to_csv("scraped_data.csv", index=True, index_label="id")

