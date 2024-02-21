'''below codes are independent of each other. each class starting with I is interface and other classes implementing these interfaces are indepndent of each other i.e. copy don't have to forcefully use scanner class if not needed.'''

class IPrinter:
    def print(self):
        pass

class IFax:
    def fax(self):
        pass

class ICopy:
    def copy(self):
        pass

class IScanner:
    def scan(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("its printing... ")

class Faxing(IFax):
    def print(self):
        print("its faxing... ")

class Copy(ICopy):
    def print(self):
        print("its copying... ")

class Scanner(IScanner):
    def print(self):
        print("its scanning... ")


