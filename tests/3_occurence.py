from models.parser import TutByParser

def average_num_test(self):
    error = ''
  #  TutByParser = parser()
    TutByParser.url = 'https://rabota.by/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=python'
    TutByParser.get_soup()
    TutByParser.get_vacancies_urls()
    TutByParser.get_wordsCount = {'python': 0, 'linux': 0, 'flask': 0}
    TutByParser.get_vacancies_urls()
    TutByParser.average_number_of_occurence()
    for key, value in TutByParser.average_number_of_occurence():
        if (value + 1) > TutByParser.get_wordsCount[key] / TutByParser.count > (value - 1):
            pass
        else:
            error += key
    assert len(error) == 0