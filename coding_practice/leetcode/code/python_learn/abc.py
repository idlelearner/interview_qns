import abc

class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class Parrot(Bird):
    pass

p = Parrot()


# virtual subclasses
@Bird.register
class Robin:
    pass

r = Robin()