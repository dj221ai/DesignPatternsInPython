import threading

class SingletonForThreadSafe:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
        

"""Here, a threading lock is used to ensure that only one thread can create the instance at a time, preventing race conditions. Leveraging lazy initialization means that the class instance is created only upon the initial object creation."""

obj=SingletonForThreadSafe()
print(obj)
obj1=SingletonForThreadSafe()
print(obj1)

