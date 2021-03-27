"""docstring"""
from bs4 import BeautifulSoup
import re


class RabotaByParser:

    @staticmethod
    def get_vacancies_urls_list(response):
        """docstring"""
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a', attrs={"class": "bloko-button HH-Pager-Control"})
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

    @staticmethod
    def get_all_page_vacancies(response)
        """docstring"""
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tags = soup.find_all('a', attrs={"class": "bloko-link HH-LinkModifier"})
        vacancy_links = []
        for tag in a_tags:
            link = tag.get('href')
            vacancy_links.append(link)
        return vacancy_links

    @staticmethod
    def get_keyword_count(response, keyword):
        """docstring"""
        soup = BeautifulSoup(response.text, 'html.parser')
        description = soup.find('div', attrs={"data-qa": "vacancy-description"})
        description_text = description.get_text()
        return description_text.lower().count(keyword.lower())
