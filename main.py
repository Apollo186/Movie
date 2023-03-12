from schedule import ReleaseSchedule
from movie import Movie
from date import Date

USER_OPTION_1 = 1
USER_OPTION_2 = 2
USER_OPTION_3 = 3
USER_OPTION_4 = 4
USER_OPTION_5 = 5
studio_name = input("What is the name of your studio? ")
user_season = input("What season do you have a schedule for? ")
user_schedule = ReleaseSchedule(studio_name,user_season)
user_choice = int(input("Enter 1 to add a movie, 2 to schedule a movie premiere, 3 to postpone a movie premiere, 4 for a summary, 5 to finish. "))

if __name__ == '__main__':
  while user_choice != USER_OPTION_5:

    if user_choice == USER_OPTION_1:
      movie_title = input("Movie Name: ")
      movie_genre = input("Genre: ")
      user_schedule.add_movie((Movie(movie_title,movie_genre)))
      
    elif user_choice == USER_OPTION_2:
      movie_title = input("Movie Name: ")
      movie_date= input('Date (mm-dd-yy): ')
      date_divided = movie_date.split('-')
      complete_date=Date(int(date_divided[0]), int(date_divided[1]),int(date_divided[2]))
      try:
        user_schedule.schedule_movie(movie_title, complete_date)
      except:
        print("Could not find movie. Please try again.")

    elif user_choice == USER_OPTION_3:
      movie_title = input("Movie Name: ")
      try:
        print('Postponed to {}'.format(user_schedule.postpone_movie(movie_title)))
      except:
        print("Could not postpone movie. Please try again.")
      
    elif user_choice == USER_OPTION_4:
      print(user_schedule.display_company_summary())
    elif user_choice != USER_OPTION_1 or user_choice != USER_OPTION_2 or user_choice != USER_OPTION_3 or user_choice != USER_OPTION_4 or user_choice != USER_OPTION_5:
      print('Try again.')
    
    user_choice = int(input("Enter 1 to add a movie, 2 to schedule a movie premiere, 3 to postpone a movie premiere, 4 for a summary, 5 to finish. "))
user_schedule.display_schedule()