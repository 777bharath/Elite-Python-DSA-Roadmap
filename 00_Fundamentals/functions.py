'''from datetime import datetime
# sample with no parameter pushing

def date():
    day=datetime.now()
    print(f"Current Date is \n {day:%x}\n")

date()


# sample with parameter pushing

def welcome(name : str):    
    print(f"Welcome {name.capitalize()}")

username=input("Enter your name\n")
welcome(username)
welcome("Bharath")

# sample with return value


def add(a : int ,b :int):
    return a + b

print(add(10 ,15))''' 


  #sample test
  # km to miles with a constatn adn type conversion
'''KM_TO_MILES = .621371

def convert_to_miles(km : int):
    return km*KM_TO_MILES

print(f"{convert_to_miles(10):.2f}")


#sample test2

def to_miles(km:int):
    return km*KM_TO_MILES

def travel_time(km: int ,speed :int):
    time: int = to_miles(km)/speed
    return time
print(f"Estimated travel rime is {travel_time(150,60):.2f}hrs")
    '''


KM_TO_MILES=.621371
BASE_CHARGE=5.0

def convert_dist(km:float):
    return km*KM_TO_MILES

def get_eta(miles:float,speed:float):
    if (speed<=0):
        raise ValueError("Speed cant be 0... like WTF")
    return miles/speed

def calc_shipping(miles:float):
    if (miles<100):
        return 0
    return (miles*0.10)+BASE_CHARGE

User_km=float(input("Enter the total distance in KM\n"))
User_speed=float(input("Enter the Avg speed in KM\n"))

miles=convert_dist(User_km)
eta=get_eta(miles,User_speed)
cost=calc_shipping(miles)

print(f"Total Distance in miles = {miles:.2f}\nTotal time taken for the shipping ={eta:.2f}hrs\nShipping cost ={cost:.2f}")



