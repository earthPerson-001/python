from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
remaining_days = []
total_data_used = []
driver.get("https://client.arrownet.com.np/main.php?pid=login_report")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': 'container'}):
    total_data_used = a.find('td', attrs={'class': 'text_12b'})
    remaining_days = a.find('td', attrs={'class': 'text_12b'})
    remaining_days.clear()
    remaining_days.append(remaining_days.txt)
    total_data_used.clear()
    total_data_used.append(total_data_used.txt)

