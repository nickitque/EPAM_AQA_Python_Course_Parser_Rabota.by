"""Test to compare keywords occurrence in all pages and in separate page"""


import pytest
from clients.http_client import HttpClient
from models.parser import RabotaByParser
from models.url_builder import UrlBuilder


@pytest.mark.parametrize("keyword", ['python', 'linux', 'flask'])
def test_avg_keyword_occurrence(avg_keyword_occurrence, keyword):
    step = 1
    vacancy_url = 'https://rabota.by/vacancy/42332824'
    vacancy_response = HttpClient.get(vacancy_url, UrlBuilder.header)
    count = RabotaByParser.get_keyword_count(vacancy_response, keyword)

    avg_occurrence = avg_keyword_occurrence[keyword]
    print(f"{keyword} average occurrence", avg_occurrence)
    assert avg_occurrence - step <= count <= avg_occurrence + step, f"Keyword '{keyword}' is not in boundaries"
