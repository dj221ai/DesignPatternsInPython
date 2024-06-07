''' we can add more shapes in the below codes without modifying the Area Calculator class which satisfies the OC principle. The code is more flexible and easy to extend with new functionalities.'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return 3.14*(self.radius**2)
    

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length * self.breadth
    


class AreaCalculator:
    def area(self, shape):
        return shape.area()
    


cobj=Circle(3)
# print(cobj.area())

robj=Rectangle(4, 5)
# print(robj.area())

acobj=AreaCalculator()
print(acobj.area(robj))
print(acobj.area(cobj))





