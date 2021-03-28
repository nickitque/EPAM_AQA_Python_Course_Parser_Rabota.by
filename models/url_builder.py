"""Module to generate urls"""


class UrlBuilder:
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/89.0.4389.90 Safari/537.36"}

    @staticmethod
    def get_base_url():
        """Getting base url"""
        return "https://rabota.by"

    @staticmethod
    def get_search_url(keyword):
        """Searching vacancies by the keyword"""
        return f"https://rabota.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text={keyword}"

    @staticmethod
    def get_vacancy_url(vacancy_id):
        """Method to get vacancy url"""
        return f"https://rabota.by/vacancy/{vacancy_id}"
