class car:

  def __init__(self, make, year_model):
    self.speed = 0
    self.make = make
    self.year_model = year_model

  def accelerate(self,speed):
    self.speed += 5

  def brake(self,speed):
    self.speed -= 5
  
  def get_speed(self):
    return  self.speed


