from clients.http_client import HTTPClient
from models.parser import TutByParser
import pytest
import re
from bs4 import BeautifulSoup

client = HTTPClient()
parserr = TutByParser()
main_script = script

@pytest.fixture()
def connection_test():
    url = parserr.get_vacancies_urls()
    response = client.get(url, headers=parserr.headers)
    return response

@pytest.fixture()
def find_shotgun_phrase():
    url = parserr.get_url(search_word="shotgun")
    response = client.get(url, headers=parserr.headers)
    return response

@pytest.fixture()
def uccurence_of_words():
    words_found1 = parserr.average_number_of_occurence(jobs_tut_by_url, search_word1, headers=parserr.headers)
    words_found2 = parserr.average_number_of_occurence(jobs_tut_by_url, search_word2, headers=parserr.headers)
    words_found3 = parserr.average_number_of_occurence(jobs_tut_by_url, search_word3, headers=parserr.headers)
    return words_found1, words_found2, words_found3

@pytest.fixture()
def grab_vacancies_list():
    url = parserr.get_vacancies_urls(search_word="python")
    response = client.get(url, headers=headers)
    vacancy_links = []
    for link in parserr.parsing_the_page(response).findAll('a', attrs={
            'href': re.compile(f"query=python")}):
        vacancy_links.append(link.get('href'))
    return vacancy_links

@pytest.fixture()
def grab_total_vacancies_list():
    url = parserr.get_vacancies_urls()
    response = client.get(url, headers=tut_by.header)
    page = parserr.parsing_the_page(response)
    num_pages = parserr.final_page(page)
    pages_links = parserr.get_vacancies_urls(url, get_all_pages)
    total_vacancies = parserr.get_vacancies_urls(pages_links, headers=parserr.headers, search_word="python")
    return total_vacancies

@pytest.fixture()
def search_number_of__vacancies():
    url = parserr.get_url(search_word="python")
    response = client.get(url, headers=parser.headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    vacs = soup.find('h1', attrs={'class': 'bloko-header-1'}).text.split()
    number = vacs[0]
    return int(number)