class Vehicle:
 def display_info(self):
    print("This is a vehicle")
class Car(Vehicle):
    def display_info(self):
        print("This is a car")
class Bike(Vehicle):
    def display_info(self):
        print("this is a Bike")
v = Vehicle()
b=Bike()
c=Car()
v.display_info()
b.display_info()
c.display_info()