from bs4 import BeautifulSoup
import requests
# from csv import writer
# import re

url= "https://www.jotform.com/app/222393442102445/222065692015451"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
lists = soup.find_all('div', class_='form-all')
print(lists)