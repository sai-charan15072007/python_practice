from abc import ABC

class Shape(ABC):
    pass
class Circle(Shape):
    def __init__(self , r):
        self.r=r
        def area(self):
            return 3.14*self.r*self.r
        class Rectangle(Shape):
            def __init__(self, l, w):
                self.l=l
                self.w=w
                def area(self):
                    return self.l*self.w

c = Circle(5)
print("Circle Area:",c.area())

r = Rectangle(10 , 5)
print("Rectangle Area:", r.area())