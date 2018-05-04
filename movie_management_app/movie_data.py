import requests
import os
# key = os.environ['OMDB_KEY']
# base_url = 'http://www.omdbapi.com/'
# def get_movie_info(name):
#     # movie_name = input('Enter movie name: ')
#     params = {'apikey':key, 't': name}
#     data = requests.get(base_url, params).json()
#     # print(data)
#     # print(data['Ratings'][0]['Value'])
#     print(data)
def get_movie_info(name):
    # apikey = 'd14fee3e'
    apikey = os.environ['OMDB_KEY']
    movie_info = {}
    url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+name
    response = requests.get(url)
    movie = response.json()
    keys = ['Title', 'Year', 'Actors', 'Director']
    for key in keys:
        movie_info.update({key: movie[key]})
    return movie_info
# year = response.json()['Year']
# released = response.json()['Released']
# movie.append(movie1)
# print('Title: ',title, 'Year: ',year, 'Released: ',released)

# return render(request, 'movie_management_app/movie.html', {'movie':movie[0]})


# def main():
#     name = input('Enter movie name: ')
#     get_movie_info(name)
#
# main()
