"""docstrings"""
from clients.http_client import HTTPClient
from models.parser import RabotaByParser

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/89.0.4389.90 Safari/537.36"}


def get_host():
    """docstring"""
    return "https://rabota.by"


def get_search_url(keyword):
    """docstring"""
    return f"https://rabota.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text={keyword}"


def print_keywords_count_per_vacancy(all_pages_list):
    """docstring"""
    for page in all_pages_list:

        page_response = HTTPClient.get(get_host() + page, header)
        assert page_response.status_code == 200

        page_vacancies_list = RabotaByParser.get_all_page_vacancies(page_response)
        for vacancy_url in page_vacancies_list:
            vacancy_response = HTTPClient.get(vacancy_url, header)
            assert vacancy_response.status_code == 200

            python_keyword_count = RabotaByParser.get_keyword_count(vacancy_response, 'python')
            linux_keyword_count = RabotaByParser.get_keyword_count(vacancy_response, 'linux')
            flask_keyword_count = RabotaByParser.get_keyword_count(vacancy_response, 'flask')

            print(vacancy_url)
            print('python=', python_keyword_count, 'linux=', linux_keyword_count, 'flask=', flask_keyword_count)


def print_keywords_average_occurrence(all_pages_list):
    """docstring"""
    vacancy_total_count = 0
    dictionary = {
        "python": 0,
        "linux": 0,
        "flask": 0
    }

    for page in all_pages_list:
        page_response = HTTPClient.get(get_host() + page, header)
        assert page_response.status_code == 200

        page_vacancies_list = RabotaByParser.get_all_page_vacancies(page_response)
        for vacancy_url in page_vacancies_list:
            vacancy_response = HTTPClient.get(vacancy_url, header)
            assert vacancy_response.status_code == 200

            vacancy_total_count += 1
            dictionary['python'] += RabotaByParser.get_keyword_count(vacancy_response, 'python')
            dictionary['linux'] += RabotaByParser.get_keyword_count(vacancy_response, 'linux')
            dictionary['flask'] += RabotaByParser.get_keyword_count(vacancy_response, 'flask')

    print('python average occurrence:', dictionary['python'] / vacancy_total_count)
    print('linux average occurrence:', dictionary['linux'] / vacancy_total_count)
    print('flask average occurrence:', dictionary['flask'] / vacancy_total_count)


def execute():
    """docstring"""
    response = HTTPClient.get(get_search_url('shotgun'), header)
    assert response.status_code == 200

    all_pages_list = RabotaByParser.get_vacancies_urls_list(response)
    print(all_pages_list)

    # print_keywords_count_per_vacancy(all_pages_list)
    print_keywords_average_occurrence(all_pages_list)


if __name__ == '__main__':
    execute()
