class vehicle:
    def __init__(self, brand,speed):
        self.brand = brand
        self.speed = speed
    def display_info(self):
        print("Brand: self.brand")
        print("Speed: self.speed")
class car(vehicle):
    def display_info(self):
            print("car Brand:", self.brand)
            print("maximum speed :",self.speed,"km/h")
class bike(vehicle):
    def display_info(self):
            print("bike Brand:", self.brand)
            print("maximum speed :",self.speed,"km/h")
car= car("hyundai",200)
bike= bike("honda",150)
car.display_info()
bike.display_info()