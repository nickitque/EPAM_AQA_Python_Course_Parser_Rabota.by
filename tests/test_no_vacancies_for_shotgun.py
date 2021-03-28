"""Test to make sure there are no vacancies for shotgun word"""


def test_no_vacancies_for_shotgun(vacancies_shotgun):
    assert vacancies_shotgun == [], "Vacancies by keyword 'shotgun' exist"
