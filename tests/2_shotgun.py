
def shotgun(find_shotgun_phrase):

    phrase = "По запросу «shotgun» ничего не найдено"
    assert find_shotgun_phrase.status_code == 200
    assert phrase in find_shotgun_phrase.text