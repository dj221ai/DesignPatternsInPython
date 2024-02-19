"""
    creating abstract classes in python

"""

from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color):
        self.color=color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # but this method is implemented here so doesn't have to be impleted at other places
    def description(self):
        print(f"{self.__class__.__name__} has {self.color} color")
        

class Rectangle(Shape):

    def __init__(self, length, breadth, color):
        super().__init__(color)
        self.breadth=breadth
        self.length=length

    def area(self):
        print(f"area is {self.length * self.breadth}")
        # return self.length * self.breadth

    def perimeter(self):
        print(f"perimeter is {(self.length + self.breadth)*2}")
        # return (self.length + self.breadth)*2



rectangle=Rectangle(5,3,"green")
rectangle.area()
rectangle.perimeter()

