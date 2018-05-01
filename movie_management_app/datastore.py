import sqlite3, os
from movie_management_app import movie_data

db_name = 'movie.db'

def add_to_db():
    #TODO: add data to database.
    movie = get_movie_info()
    create_movieInfo_table()
    add_data_to_movieInfo_table()

def create_movieInfo_table():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('CREATE TABLE IF NOT EXIST watch_list (ID PRIMARY KEY INT, Name TEXT, Actor TEXT, Director Text, Year TEXT) ')

def add_data_to_movieInfo_table(name, actor, director, year):
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        sql_statement = 'INSERT INTO watch_list VALUES (?,?,?,?,?)'
        cur.execute(sql_statement, (None, name, actor, director, year))
