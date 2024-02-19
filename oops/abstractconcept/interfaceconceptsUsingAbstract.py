"""
    1. Python does not have strict interface concept so we use abstract method in place 
    2. import abstracgt classes than all children will have to implement all of abstract methods.
    3. In an interface, methods have no implementation so we use pass.
"""

from abc import ABC, abstractmethod

class MyInterface(ABC):

    # def __init__(self):
    #     print("constructor from interface!!!")
    
    @abstractmethod
    def abs_method(self):
        pass


class MyExampleClassOne(MyInterface):

    # def __init__(self, name):
    #     self.name=name
    #     print(f"{self.name}")
    #     super().__init__()

    def abs_method(self):
        print("abs method from my example class one")


class MyClassTwo(MyInterface):

    def abs_method(self):
        print("abs from class 2")


one=MyExampleClassOne("abcd")
one.abs_method()


