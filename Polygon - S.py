class Polygon:
    def __init__(self, numSides):
        self.numSides = numSides
        self.units = ""
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

    def GetUnits(self):
        self.units = input("Enter the units: ")


class Rectangle(Polygon):
    def __init__(self):
        # automatically sets the __init__ to have 2 sides
        Polygon.__init__(self, 2)

    def getArea(self):
        side1, side2 = self.sides
        if side1 is None and side2 is None:
            print("You have not entered any side lengths!\nPlease enter the side lengths in order to calculate area")
            self.EnterSL()
            self.GetUnits()
            side1, side2 = self.sides
        unitStr = self.units + "^2"
        if self.units == "":
            unitStr = ""
        print("The area of rectangle with sides", side1, "and", side2, "is", side1 * side2, unitStr)
        # add an get perimeter method make sure to implement the feature to check if the user has entered any side lengths


b24 = Rectangle()
b24.getArea()
