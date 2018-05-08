import requests
import os

def get_movie_info(name):
    apikey = os.environ['OMDB_KEY']
    movie_info = {}
    url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+name
    response = requests.get(url)
    movie = response.json()
    keys = ['Title', 'Year', 'Actors', 'Director']
    for key in keys:
        movie_info.update({key: movie[key]})
    return movie_info
