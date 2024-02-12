class MetaSingleton(type):
    """ Creating Single using meta classes """

    _instances={}

    def __call__(cls, *args, **kwargs):
        """
            Possible changes to the value of the `__init__` argument
            do not affect the returned instance.
        """

        if cls not in cls._instances:
            instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        
        return cls._instances[cls]
    

class Singleton(metaclass=MetaSingleton):

    def __init__(self):
        pass

    def mtdOne(self):
        return "Method One"
    

obj=Singleton()
print(obj)
obj1=Singleton()
print(obj1)
