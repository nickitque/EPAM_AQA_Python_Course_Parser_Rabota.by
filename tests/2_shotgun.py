import requests
from bs4 import BeautifulSoup

#def finding_the_phrase(header)
url = 'https://rabota.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text=shotgun'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text="По запросу «shotgun» ничего не найдено")
output = ''
blacklist = []

for t in text:
    if t.parent.name not in blacklist:
        output = '{} '.format(t)

assert("По запросу «shotgun» ничего не найдено")
