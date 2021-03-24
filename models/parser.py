import re
from bs4 import BeautifulSoup
from clients.http_client import HTTPClient

http_client = HTTPClient()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class TutByParser:
    @staticmethod
    def parsing_the_page(resp):
        soup = BeautifulSoup(text.text, 'html.parser')
        return soup

    @staticmethod
    def get_vacancies_urls(url: str, get_all_pages, int):
        urls = []
        for page in get_all_pages():
            response = requests.get(page, headers=headers)
            for url in parsing_the_page(response).findAll('a', attrs={'href': re.compile("query=python")}):
                urls.append(url.get('href'))
        return urls

    @staticmethod
    def final_page():
        url = []
        for ln in parsing_vacansies_list(response).findAll('a', attrs={'href': re.compile("page=\d$")}):
            url.append(ln.get('href'))
        return int(url[-2][-1]) +1


    def get_wordsCount(self, text, search_word1: str, search_word2: str, search_word3: str):
        end_list = []
        for i in text:
            scan_url = http_client.get(url, headers)
            vacancy_id = url[26:34]
            words_found1 = re.findall(search_word1.lower()),parsing_the_page(scan_url).get_text(" ".lower())
            words_found2 = re.findall(search_word2.lower()), parsing_the_page(scan_url).get_text(" ".lower())
            words_found3 = re.findall(search_word3.lower()), parsing_the_page(scan_url).get_text(" ".lower())

            found1 = len(words_found1)
            found2 = len(words_found2)
            found3 = len(words_found3)

            res = {'Vacancy id': vacancy_id, search_word1: found1, search_word2: found2, search_word3: found3}
            end_list.append(res)
        return end_list


    def get_all_pages():
        page_urls = []
        for i in range(final_page()):
            url = "https://rabota.by/search/vacancy?L_is_autosearch=false&area=1002&" \
             f"clusters=true&enable_snippets=true&text=python&page={i}"
            page_urls.append(url)
        return page_urls

    @staticmethod
    def average_number_of_occurence (average_number, word1, word2, word3):
        total_vacancies = len(average_number)
        total_words1 = 0
        total_words2 = 0
        total_words3 = 0
        for i in result_list:
            total_words1 += i[word1]
            total_words2 += i[word2]
            total_words3 += i[word3]

        average_num = f"{word1} average: {round((total_words1 / total_vacancies), 2)}" \
              f"{word2} average: {round((total_words2 / total_vacancies), 2)}\n" \
              f"{word3} average: {round((total_words3 / total_vacancies), 2)}"
        return average_num
