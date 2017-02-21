typeProb = int(input())
totalCit = int(input())
spDin = input()
spPin = input()

speedsOfP = [int(x) for x in spPin.split(" ")]
speedsOfD = [int(x) for x in spDin.split(" ")]

solutions = []
if typeProb == 1:
    for i in range(len(speedsOfD)):
        firstMax = max(speedsOfD)
        speedsOfD.remove(firstMax)
        secondMax = max(speedsOfP)
        speedsOfP.remove(secondMax)
        solutions.append([firstMax, secondMax])
    mini = 0
    for i in solutions:
        mini += max(i)
    print(mini)

else:
    for i in range(len(speedsOfD)):
        firstMax = max(speedsOfD)
        secondMax = max(speedsOfP)
        if firstMax > secondMax:
            smallestP = min(speedsOfP)
            solutions.append([firstMax, smallestP])
            speedsOfD.remove(firstMax)
            speedsOfP.remove(smallestP)
        else:
            smallestD = min(speedsOfD)
            solutions.append([secondMax, smallestD])
            speedsOfD.remove(smallestD)
            speedsOfP.remove(secondMax)

    bigOrSmall = 0
    for i in solutions:
        bigOrSmall += max(i)
    print(bigOrSmall)
