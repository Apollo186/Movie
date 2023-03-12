class Movie:
  def __init__(self,title:str,genre:str):
    self.title = title
    self.genre= genre

  def __str__(self) -> str:
    return f"{self.title}, {self.genre}"