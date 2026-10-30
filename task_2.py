catalog = [
{"title": "Мастер и Маргарита", "author": "Булгаков",
"year": 1967, "genre": "роман", "on_loan": True},
{"title": "Евгений Онегин", "author": "Пушкин",
"year": 1833, "genre": "роман", "on_loan": False},
{"title": "Стихотворения", "author": "Есенин",
"year": 1926, "genre": "поэзия", "on_loan": False},
{"title": "Вишнёвый сад", "author": "Чехов",
"year": 1904, "genre": "пьеса", "on_loan": True},
{"title": "Руслан и Людмила", "author": "Пушкин",
"year": 1820, "genre": "поэма", "on_loan": False},
{"title": "Три сестры", "author": "Чехов",
"year": 1901, "genre": "пьеса", "on_loan": False},
]

def find_by_author(catalog, author):
    ans = []
    for i in range(len(catalog)):
        if author in catalog[i].values():
            ans.append(catalog[i]["title"])
    return ans

def available_titles(catalog):
    ans = []
    for i in range(len(catalog)):
        if catalog[i]["on_loan"] == False:
            ans.append(catalog[i]["title"])
    return ans

def books_grouped_by_genre(catalog):
    groups={}
    for group in catalog:
        for i in range(len(catalog)):
            key = catalog[i]["genre"]
            if key not in groups:
                groups[key] = []
            if catalog[i]["title"] not in groups[key]: groups[key].append(catalog[i]["title"])
    return groups