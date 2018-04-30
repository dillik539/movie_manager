import requests
import os
key = os.environ['OMDB_KEY']
base_url = 'http://www.omdbapi.com/'
def get_movie_info(name):
    # movie_name = input('Enter movie name: ')
    params = {'apikey':key, 't': name}
    data = requests.get(base_url, params).json()
    # print(data)
    # print(data['Ratings'][0]['Value'])
    print(data)
def main():
    name = input('Enter movie name: ')
    get_movie_info(name)

main()
