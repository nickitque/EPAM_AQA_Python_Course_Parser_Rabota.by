"""Test to check that there is no vacancy with url /invalid"""


import pytest


@pytest.mark.parametrize('vacancy_id', ["invalid"])
def test_vacancy_does_not_exists(vacancy_exists):
    assert bool(vacancy_exists['title']) is False, "Vacancy title is not empty"
    assert bool(vacancy_exists['description']) is False, "Vacancy description is not empty"
