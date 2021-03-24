
import requests
import re
from clients.http_client import HTTPClient

http_client =HTTPClient()

response = http_client(url)

vacancies_urls = get_vacancies_urls(url)

parsing = parsing_vacansies_list (response)

tut_by = TutByParser


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

jobs_tut_by_url = "https://rabota.by/search/vacancy"
params = {
    "area=1002"
    "fromSearchLine": "true",
    "st": "searchVacancy",
    "text": "python"
}

if __name__ == '__main__':
    result = tut_by.get_wordsCount(vacancies_urls, "Python", "Linux",
                                        "Flask", header)
    average = tut_by.average_number_of_occurence(result, "Python", "Linux",
                                               "Flask")



