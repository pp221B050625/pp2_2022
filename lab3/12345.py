movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


def above():
    m = input()
    for i in movies:
        if i["name"] == m:
            if i["imdb"] > 5.5:
                return True


def above_list():
    l = []
    for i in movies:
        if i["imdb"] > 5.5:
            l.append(i["name"])
    return l


def category_list():
    l = []
    c = input()
    for i in movies:
        if i["category"] == c:
            l.append(i["name"])
    return l


def avg():
    tot = 0
    div = 0
    l = input().split()
    for j in l:
        for i in movies:
            if j == i["name"]:
                tot += i["imdb"]
                div += 1
    return tot / div


def cat_avg():
    tot = 0
    div = 0
    c = input()
    for i in movies:
        if i["category"] == c:
            tot += i["imdb"]
            div += 1
    return tot / div


