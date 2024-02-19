from abc import ABC, abstractmethod
from typing import Type


class MyInterface(ABC):
    @abstractmethod
    def mtd(self):
        pass


class ClassOne(MyInterface):
    def mtd(self):
        print("calling method from class one")


class ClassTwo(MyInterface):
    def mtd(self):
        print("Calling mtd from class two!")



class NotImplementingInterface:
    def mtd1(self):
        print("no interface implementor!!!")


def interface_processor(obj: MyInterface):
    obj.mtd()
    print("Interface implementing object!!")





cone=ClassOne()
# cone.mtd()
ctwo=ClassTwo()
# ctwo.mtd()

noInt_obj=NotImplementingInterface()

interface_processor(cone)
interface_processor(ctwo)
interface_processor(noInt_obj)



