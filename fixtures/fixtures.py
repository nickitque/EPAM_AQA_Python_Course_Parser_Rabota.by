from pytest import fixture
from clients.http_client import HttpClient
from models.parser import RabotaByParser
from models.url_builder import UrlBuilder


@fixture
def connection():
    """Module to get status code"""
    response = HttpClient.get(UrlBuilder.get_base_url(), UrlBuilder.header)
    return response


@fixture
def vacancies_shotgun():
    """Module to inspect there are no vacancies for shotgun word"""
    response = HttpClient.get(UrlBuilder.get_search_url('shotgun'), UrlBuilder.header)
    vacancies_links = RabotaByParser.get_vacancies_urls_list(response)
    return vacancies_links


@fixture(scope='session')
def avg_keyword_occurrence():
    """Module to count average occurrence of keywords"""
    response = HttpClient.get(UrlBuilder.get_search_url('python'), UrlBuilder.header)
    keywords_occurrence = RabotaByParser.get_keywords_average_occurrence(response)
    return keywords_occurrence


@fixture
def vacancy_exists(vacancy_id):
    """Module to check that vacancy exists or not"""
    response = HttpClient.get(UrlBuilder.get_vacancy_url(vacancy_id), UrlBuilder.header)
    vacancy_data = RabotaByParser.parse_vacancy(response.text)
    return vacancy_data


@fixture
def vacancy_per_page():
    """Module to count vacancies per page"""
    page_response = HttpClient.get(UrlBuilder.get_search_url('python'), UrlBuilder.header)
    vacancies_url_list = RabotaByParser.get_all_page_vacancies(page_response)
    return len(vacancies_url_list)
