__author__ = 'Javier'

import requests     # Hay que cargar esta libreria antes de usarla con "pip install requests" en la terminal.
import sqlite3


class Database(object):

    def __init__(self):
        self._conn = sqlite3.connect("movies")
        self._cursor = self._conn.cursor()

    def read_from_database(self, movie_name):
        print("Reading.....")
        self._cursor.execute("SELECT * FROM movies WHERE name = '"+movie_name+"';")
        raw_data = self._cursor.fetchone()
        self._conn.close()
        return raw_data

    def save_in_database(self, movie_data):
        print("Saving.....")
        self._cursor.execute("INSERT INTO movies VALUES('"+movie_data['Title']+"','"+movie_data['Year']+"');")
        self._conn.commit()
        self._conn.close()

    def list_from_database(self,):
        list_from = self._cursor.execute("SELECT * FROM movies")
        return list_from


class RestMovies(object):

   def read_from_rest(self, movie_name):
       #"http://www.omdbapi.com/?t=birdman"
       raw_data = requests.get("http://www.omdbapi.com/", params={'t': movie_name})
       movie_info = raw_data.json()
       return movie_info


class InfoPeliculas(object):

    def __init__(self, db, rest_service):
        self._db = db
        self._rest_service = rest_service

    def recover_movie(self, movie_name):
        movie_info = self._db.read_from_database(movie_name)
        if movie_info == None:
            movie_info = self._rest_service.read_from_rest(movie_name)
            self._db.save_in_database(movie_info)
        return movie_info

    def list_movie(self):
        print("Listing.....")
        return self._db.list_from_database()



if __name__ == "__main__":
    print("Running")
    info = InfoPeliculas(Database(), RestMovies())
    #movie1 = info.recover_movie("Frozen")
    # movie2 = info.recover_movie("Big")
    movie_list = info.list_movie()
    print(type(movie_list))
    # print(type(info._rest_service))
    print("ok")
