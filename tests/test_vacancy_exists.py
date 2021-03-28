"""Test to check that separate vacancy exists and have Title and Description"""


import pytest


@pytest.mark.parametrize('vacancy_id', ["42332824"])
def test_vacancy_exists(vacancy_exists):
    assert bool(vacancy_exists['title']), "Vacancy title is empty"
    assert bool(vacancy_exists['description']), "Vacancy description is empty"
