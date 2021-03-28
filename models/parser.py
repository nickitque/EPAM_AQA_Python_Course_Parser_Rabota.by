"""Module for parsing Rabota.By"""


from bs4 import BeautifulSoup
import re

from clients.http_client import HttpClient
from models.url_builder import UrlBuilder


class RabotaByParser:

    @classmethod
    def get_vacancies_urls_list(cls, response):
        """Method to get list of vacancies urls"""
        soup = BeautifulSoup(response.text, 'html.parser')
        not_found_header = soup.find('h1', attrs={"data-qa": "bloko-header-1"})
        if not_found_header and not_found_header.text.find('ничего не найдено') > 0:
            return []
        a_tags = soup.find_all('a', attrs={"class": "bloko-button HH-Pager-Control"})
        if not a_tags:
            return []
        max_page_number = 0
        for tag in a_tags:
            link = tag.get('href')
            number = int(re.findall('page=\\d+', link)[0].replace('page=', ''))
            if number > max_page_number:
                max_page_number = number
        template = a_tags[0].get('href')
        links = []
        for i in range(max_page_number + 1):
            uri = re.sub('page=\\d+', 'page=' + str(i), template)
            links.append(uri)
        return links

    @classmethod
    def get_all_page_vacancies(cls, response):
        """Method to get all pages with vacancies"""
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a', attrs={"class": "bloko-link HH-LinkModifier"})
        vacancy_links = []
        for tag in a_tags:
            link = tag.get('href')
            vacancy_links.append(link)
        return vacancy_links

    @classmethod
    def get_keywords_average_occurrence(cls, response):
        """Method to count average occurrence of keywords"""
        all_pages_list = cls.get_vacancies_urls_list(response)

        vacancy_total_count = 0
        dictionary = {
            "python": 0,
            "linux": 0,
            "flask": 0
        }
        if len(all_pages_list) > 0:
            for page in all_pages_list:
                page_response = HttpClient.get(UrlBuilder.get_base_url() + page, UrlBuilder.header)

                page_vacancies_list = cls.get_all_page_vacancies(page_response)
                for vacancy_url in page_vacancies_list:
                    vacancy_response = HttpClient.get(vacancy_url, UrlBuilder.header)

                    vacancy_total_count += 1
                    dictionary['python'] += cls.get_keyword_count(vacancy_response, 'python')
                    dictionary['linux'] += cls.get_keyword_count(vacancy_response, 'linux')
                    dictionary['flask'] += cls.get_keyword_count(vacancy_response, 'flask')
            if vacancy_total_count > 0:
                dictionary['python'] = dictionary['python'] / vacancy_total_count
                dictionary['linux'] = dictionary['linux'] / vacancy_total_count
                dictionary['flask'] = dictionary['flask'] / vacancy_total_count

        return dictionary

    @classmethod
    def get_keyword_count(cls, vacancy_response, keyword):
        """Method to count keywords"""
        soup = BeautifulSoup(vacancy_response.text, 'html.parser')
        description = soup.find('div', attrs={"data-qa": "vacancy-description"})
        description_text = description.get_text()
        return description_text.lower().count(keyword.lower())

    @classmethod
    def parse_vacancy(cls, html):
        """Method to parse title and description of vacancy"""
        vacancy_data = {
            "title": '',
            "description": ''
        }
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1', attrs={"data-qa": "vacancy-title"})
        description = soup.find('div', attrs={"data-qa": "vacancy-description"})
        if title:
            vacancy_data['title'] = title.text
        if description:
            vacancy_data['description'] = description.text
        return vacancy_data
