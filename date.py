class Date:
  def __init__(self,month:int,day:int,year:int):
    self.month = month
    self.day = day
    self.year = year

  def __str__(self) -> str:
    return f"{self.month}-{self.day}-{self.year}"