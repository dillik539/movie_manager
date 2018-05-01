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

apikey = 'd14fee3e'
movie = []
# if 'search_movie' in request.GET:
    # title = request.GET.get('search_movie')
    # print(title)
name = input('Enter movie name: ')
url = 'http://www.omdbapi.com/?apikey='+apikey+'&'+'t='+name
response = requests.get(url)
movie1 = response.json()['Title']
movie2 = response.json()['Year']
movie3 = response.json()['Released']
movie.append(movie1)
print('Title: ',movie1, 'Year: ',movie2, 'Released: ',movie3)

# return render(request, 'movie_management_app/movie.html', {'movie':movie[0]})


# def main():
#     name = input('Enter movie name: ')
#     get_movie_info(name)
#
# main()
