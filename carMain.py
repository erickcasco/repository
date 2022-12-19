import car

mycar = car.car("scionXB", "2003")

def main():
  
  print("The car is now made.")
  print("The car's current speed is:")
  print("speedometer: ", mycar.speed)
  
  print("The car is speeding up.")
  for i in range(5):
    mycar.accelerate(mycar.speed)
    mycar.get_speed()
    print("speedometer: ", mycar.speed)
    
  print("The car is slowing down.")
  for i in range(5):
    mycar.brake(mycar.speed)
    mycar.get_speed()
    print("speedometer: ", mycar.speed)
    
main()    
