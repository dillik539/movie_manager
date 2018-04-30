import sqlite3, os
from movie_management_app import movie_data

db_name = 'movie.db'

def add_to_db(db_nam):
    #TODO: add data to database.

def create_movieInfo_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('CREATE TABLE IF NOT EXIST watch_list (ID PRIMARY KEY INT, Name TEXT, Actor TEXT, Director Text, Date_released TIMESTAMP) ')
