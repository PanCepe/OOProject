
class Animal:
    number_of_animals = 0
    def __init__(self, name, colour, number_of_legs):
        self.name = name
        self.colour = colour
        self.number_of_legs = number_of_legs
        Animal.number_of_animals += 1

class Mammal(Animal):

    def __init__(self, name, colour, number_of_legs=-1):
        super().__init__(name, colour, number_of_legs)

class Dog(Mammal):
    number_of_dogs = 0

    def __init__(self, name, colour):
        super().__init__(name, colour, 4)

class Cat(Mammal):
    number_of_cats = 0
    def __init__(self, name, colour):
        super().__init__(name, colour, 4)

class Bird(Animal):
    number_of_birds = 0
    def __init__(self, name, colour):
        super().__init__(name, colour, 2)
        bird.number_of_birds += 1

class Fish(Animal):
    number_of_fish = 0
    def __init__(self, name, colour):
        super().__init__(name, colour, 0)
        fish.number_of_fish += 1














