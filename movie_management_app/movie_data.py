import requests
import os

key = os.environ['OMDB_KEY']
base_url = 'http://www.omdbapi.com/'
movie_name = input('Enter movie name: ')
params = {'apikey':key, 't': movie_name}
data = requests.get(base_url, params).json()
print(data)
print(data['Ratings'][0]['Value'])
