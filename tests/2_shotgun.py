import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#def finding_the_phrase(header)
url = 'https://rabota.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text=shotgun'
res = requests.get(url, headers=headers)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text="По запросу «shotgun» ничего не найдено")
output = ''
blacklist = []

for t in text:
    if t.parent.name not in blacklist:
        output = '{} '.format(t)

print(output)

