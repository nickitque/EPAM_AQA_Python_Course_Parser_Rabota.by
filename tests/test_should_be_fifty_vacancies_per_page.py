"""Test to check that there are 50 vacancies in the list of the page"""


def test_should_be_fifty_vacancies_per_page(vacancy_per_page):
    assert vacancy_per_page == 50, "Vacancy quantity isn't equal fifty"
