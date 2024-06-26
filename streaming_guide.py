# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 05/30/2024
# Description: Program that is a movie streaming guide

class Movie:
    def __init__(self, _title, _genre, _director, _year):
        '''Initialize a Movie object'''
        self._title = _title
        self._genre = _genre
        self._director = _director
        self._year = _year

    def get_title(self):
        '''Get the title of a movie'''
        return self._title
    
    def get_genre(self):
        '''Get the genre of a movie'''
        return self._genre
    
    def get_director(self):
        '''Get the director of a movie'''
        return self._director
    
    def get_year(self):
        '''Get the year the movie was released'''
        return self._year

class StreamingService:
    def __init__(self, _name):
        '''Initialize the StreamingService object'''
        self._name = _name
        self._catalog = {}
    
    def get_name(self):
        '''Get the name of the streaming service'''
        return self._name

    def get_catalog(self):
        '''Get the catalog of movies offered on the streaming service'''
        return self._catalog

    def add_movie(self, movie):
        '''Adds a movie to the streaming service catalog'''
        self._catalog[movie.get_title()] = movie
    
    def delete_movie(self, _title):
        '''Deletes a movie from the streaming service catalog by title'''
        if _title in self._catalog:
            del self._catalog[_title]

class StreamingGuide:
    def __init__(self):
        '''Initialize the StreamingGuide object'''
        self._streaming_services = []

    def add_streaming_service(self, streaming_service):
        '''Add a streaming service to the guide'''
        self._streaming_services.append(streaming_service)
    
    def delete_streaming_service(self, _name):
        '''Deletes a streaming service from the guide by name'''
        self._streaming_services = [_service for _service in self._streaming_services if _service.get_name() != _name]

    def where_to_watch(self, _title):
        '''Find what streaming service has a specific movie'''
        services_with_movie = []
        for _service in self._streaming_services:
            if _title in _service.get_catalog():
                services_with_movie.append(_service.get_name())
        
        if not services_with_movie:
            return None

        movie = None
        for _service in self._streaming_services:
            if _title in _service.get_catalog():
                movie = _service.get_catalog()[_title]
                break
        
        if movie:
            movie_info = f"{movie.get_title()} ({movie.get_year()})"
            return [movie_info] + services_with_movie
        else:
            return None

# movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
# movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
# movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
# movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

# stream_serv_1 = StreamingService('Netflick')
# stream_serv_1.add_movie(movie_2)

# stream_serv_2 = StreamingService('Hula')
# stream_serv_2.add_movie(movie_1)
# stream_serv_2.add_movie(movie_4)
# stream_serv_2.delete_movie('The Seventh Seal')
# stream_serv_2.add_movie(movie_2)

# stream_serv_3 = StreamingService('Dizzy+')
# stream_serv_3.add_movie(movie_4)
# stream_serv_3.add_movie(movie_3)
# stream_serv_3.add_movie(movie_1)

# stream_guide = StreamingGuide()
# stream_guide.add_streaming_service(stream_serv_1)
# stream_guide.add_streaming_service(stream_serv_2)
# stream_guide.add_streaming_service(stream_serv_3)
# stream_guide.delete_streaming_service('Hula')
# search_results = stream_guide.where_to_watch('Little Women')

# print(search_results)
