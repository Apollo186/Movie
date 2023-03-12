from movie import Movie
from date import Date
from movie_not_found_error import MovieNotFoundError

class ReleaseSchedule:
  def __init__(self,studio_name:str,season:str):
    self.studio_name = studio_name
    self.season = season
    self.movie_list = []
    self.schedule_dict = {}
  
  
  def add_movie(self,movie_list: Movie):
      self.movie_list.append(movie_list)
      
  
  def schedule_movie(self,movie_title:str,movie_date:Date):
    movie_exist = False
    for movie in self.movie_list:
      if movie_title in movie.title:
        movie_exist = True
    if movie_exist == True:
        self.schedule_dict[movie_title] = movie_date
    else:
      raise MovieNotFoundError("Could not find movie. Please try again.")




  def postpone_movie(self,movie_title:str) -> Date:
    if movie_title in self.schedule_dict:
      preimere_date = self.schedule_dict[movie_title]
      postponed_premiere_date = Date(preimere_date.month,preimere_date.day,preimere_date.year + 1)
      self.schedule_dict[movie_title] = postponed_premiere_date
      return postponed_premiere_date
    else:
      raise MovieNotFoundError("Could not postpone movie. Please try again.")

  
  def display_company_summary(self):
    print(self.studio_name)
    if len(self.schedule_dict) == len(self.movie_list):
      return('{}: {} movie premieres'.format(self.season,len(self.movie_list)))
    else:
      premieres_scheduled = len(self.movie_list) - len(self.schedule_dict)
      return('{}: {} movie premieres ({} to be scheduled)'.format(self.season,len(self.movie_list),premieres_scheduled))


  def display_schedule(self):
    print(self.studio_name,self.season)
    for movies in self.movie_list:
      print(movies)
      if movies.title in self.schedule_dict:
        dates_for_movies = self.schedule_dict[movies.title]
        print(dates_for_movies)
      else:
        print("To Be Scheduled")
    print()
             
    
    
