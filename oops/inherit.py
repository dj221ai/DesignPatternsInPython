class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print(f"{self.name} makes different sounds!")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} always barks!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} always meows!")


dog=Dog("Tommy")
cat=Cat("Ketty")
dog.speak()
cat.speak()