from time import sleep, time
from random import choice


class Dog:
    def __init__(self, name, breed, color, weightKg, gender):
        self.breed = breed
        self.name = name
        self.gender = gender
        self.color = color
        self.weight = weightKg
        self.birthday = time()  # strftime('%S')

    def age(self):
        age = int(time()) - int(self.birthday)
        print(self.name, "is", age, "seconds old")

    def bark(self):
        for i in range(0, (int(self.weight / 2))):
            print(choice(["Woof", "Grr", "howl", "arf", "ruff", "bow-wow"]))
            c = choice([0, 2, 3, 1, 5])
            sleep(c)
            # print(c)

    def feed(self, foodGrams):
        self.weight += (foodGrams / 1000) / 2

    def meet(self, other):
        print(self.name, "meet", other.name, "in the dog park")

        if other.gender == "Male" and self.gender == "Female":
            print(self.name, "has a crush on", other.name)
        else:
            print(self.name, "and", other.name, "are going to play chase")


Yorkie = Dog("JJ", "Yorkie", "Tan", 2, "Male")
Yorkie.bark()
Yorkie.age()
Yorkie.feed(100)
print("My Yorkie weighs", Yorkie.weight, "Kg")

GermanShep = Dog("Jenny", "German Shepard", "Brown", 29, "Female")
GermanShep.meet(Yorkie)