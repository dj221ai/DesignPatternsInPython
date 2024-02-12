class Singleton:
    _instance=None

    def __new__(cls):
        # In this example, the __new__ method is overridden to ensure that only one instance of the class is created. If the instance does not exist, a new one is created, otherwise, the existing instance is returned.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    

obj = Singleton()
print(obj)
obj1=Singleton()
print(obj1)
