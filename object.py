class Animal:
    def make_sound(self):
        pass


class dog(Animal):
    def make_sound(self):
        return "woof"

class cat (Animal):
    def make_sound(self):
        return "Meow"

animals = [dog(), cat()]

for animal in animals:
    print(animal.make_sound())

