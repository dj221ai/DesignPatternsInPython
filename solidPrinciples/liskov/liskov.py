'''FlyingBird and NonFlyingBird both inherit bird class but both  provide alternative implementation of fly method and ostrich and parrot inherit from respective classes which satiesfies LSP any subclasses of bird can now be substituted without altering the correctness of a program.'''

class Bird:
    def fly(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        print("I can Flyyyy!!")


class NonFlyingBird(Bird):
    def fly(self):
        print("I can't Fly!! ")



class Ostrich(NonFlyingBird):
    pass
    # def fly(self):
    #     return super().fly()


class Parrot(FlyingBird):
    pass
    


ostobj=Ostrich()
ostobj.fly()

pobj=Parrot()
pobj.fly()




