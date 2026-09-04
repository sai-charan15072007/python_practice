from abc import ABC,abstractmethod
class Shape(ABC):
class Circle(Shape):
    def __init__(self,r):
    self.r=r
    def area(self):
    return 3.14*self.r*self.r
class rectangle(Shape):
    def __init__(self,l,w):            
    self.l=l
    self.w=w
    def area(self):
    return self.l*self.w
shapes = [Circle(5),rectangle(4,6)]
for shape in shapes:
print(Shape.area())
                    