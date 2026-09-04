form abc import ABC, abstractmethod 
class shape(ABC):

    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    class rectangle(shape):
        def __init__(self, l,w):
            self.l=l
            self.w=w
        def area(self):
            return self.l*self.w
shapes =[
circle(5)
rectangle(4, 6)
]
for shape in shapes:
    print(shape.area())

