class Polygon:
    def __init__(self, numSides):
        self.numSides = numSides
        self.sides = [None for i in range(numSides)]  # List comprehension
        # essentially it is a for loop:
        # self.listt = []
        # for i in range(numSides):
        #     self.listt.append(None)

    def EnterSL(self):
        self.sides = []
        for i in range(self.numSides):
            sideLength = float(input("Please enter the length of side " + str(i + 1) + ": "))
            self.sides.append(sideLength)

    def dispSides(self):
        for i in range(self.numSides):
            print("Side", i + 1, "is", self.sides[i])


class Rectangle(Polygon):
    def __init__(self):
        # automatically sets the __init__ of rectangle to have 2 sides
        Polygon.__init__(self, 2)

    def getArea(self):
        s1, s2 = self.sides
        if s1 is None and s2 is None:
            print("You have not entered any side lengths!\nPlease enter the side lengths in order to calculate area")
            self.EnterSL()
            s1, s2 = self.sides
        print("The area of rectangle with sides", s1, "and", s2, "is", s1 * s2)
    # add an get perimeter method make sure to implement the feature to check if the user has entered any side lengths


# add another class
b24 = Rectangle()
b24.EnterSL()
b24.getArea()
