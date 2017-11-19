import requests
import collections

MovieResult = collections.namedtuple(
        'MovieResult',
        "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")


def find_movies(search_text):
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    # print(type(movie_data), movie_data)

    # movies= []
    # for md in movies_list:
    #     m = MovieResult(
    #         imdb_code=md.get('imdb_code'),
    #         title = md.get('title'),
    #         duration = md.get('duration'),
    #         director = md.get('director'),
    #         year = md.get('year',0),
    #         rating = md.get('rating',0),
    #         imdb_score = md.get('imdb_score',0.0),
    #         keywords = md.get('keywords'),
    #         genres=md.get('genres')
    #     )
    #     movies.append(m)


    # All of the above can be replaced witht he code below. As long as the headers match the key.
    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    movies.sort(key=lambda m: -m.year)

    return movies