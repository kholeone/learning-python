from abc import abstractmethod

class Bird:
    fly = True

    def noise(self):
        print("Birdnoise")

    babies = 0

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False