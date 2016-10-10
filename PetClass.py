from time import sleep, time
from random import choice


class Pet:
    def __init__(self, name, age, weightKG, eyeColor, gender, microChipNum):
        self.name = name
        self.age = age
        self.weight = weightKG
        self.eyeColor = eyeColor
        self.birthday = time()
        self.gender = gender
        self.microChipNum = microChipNum

    def do_business(self):
        print(self.name, "went to the outside to do their business")


class dog(Pet):
    def dog_identity(self):
        print(self.name, "is a", self.gender.lower(), "and weighs", self.weight, "kilograms")

    def age(self):
        age = int(time()) - int(self.birthday)
        print(self.name, "is", age, "seconds old")

    def bark(self):
        for i in range(0, (int(self.weight / 2))):
            print(choice(["Woof", "Grr", "howl", "arf", "ruff", "bow-wow"]))
            c = choice([0, 2, 3, 1, 5])
            sleep(c)

    def feed(self, foodGrams):
        self.weight += (foodGrams / 1000) / 2
        #     Add a series of if statements that will print whether the dog is full based on its food intake
        if foodGrams > 500:
            print("You feed", self.name, foodGrams, "grams of food", self.name, "is full")

    def meet(self, other):
        print(self.name, "meet", other.name, "in the dog park")

        if other.gender == "Male" and self.gender == "Female":
            print(self.name, "has a crush on", other.name)
        else:
            print(self.name, "and", other.name, "are going to play chase")


class bird(Pet):
    def do_business(self):
        # overwrites existing method as birds do business in their cage
        print(self.name, "did it's business in its cage")

class cat(Pet):
    def sleep(self):
        print("sleep")
# Add method that overwrites the do business to print that name went to the litter box
# Add more methods to the cat class




hazel = dog("Haze", 1, 12, "Golden", "Male", 123456789)
hazel.dog_identity()
hazel.feed(501)
tweety = bird("Parrot",3,45,"red","male", 890890890)
tweety.do_business()