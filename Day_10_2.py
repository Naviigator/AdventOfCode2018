class Point:
    idGiver = 0
    def __init__(self, x, y):
        self.id = Point.idGiver
        Point.idGiver += 1
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(id)

def solve(inputList):
    positionAndVelocity = {}
    for entry in inputList:
        entryList = entry.split("<")
        xAndY = entryList[1].split(",")
        x = int(xAndY[0])
        y = int(xAndY[1].split(">")[0])
        velXAndY = entryList[2].split(",")
        velX = int(velXAndY[0])
        velY = int(velXAndY[1].split(">")[0])
        positionAndVelocity[Point(x, y)] = (velX, velY)

    initialTime = calculateOptimalStartingTime(positionAndVelocity)

    step(positionAndVelocity, initialTime)
    timeSpent = initialTime
    manhattanDistance = getManhattanDistance(positionAndVelocity)
    previousManhattanDistance = getManhattanDistance(positionAndVelocity)
    forward = True
    while previousManhattanDistance > manhattanDistance or forward:
        if previousManhattanDistance < manhattanDistance:
            forward = False

        previousManhattanDistance = manhattanDistance
        stepSize = 1
        if not forward:
            stepSize = stepSize * -1
        step(positionAndVelocity, stepSize)
        timeSpent += stepSize
        manhattanDistance = getManhattanDistance(positionAndVelocity)

    step(positionAndVelocity, 1)
    return timeSpent + 1


def step(positionAndVelocity, stepSize):
    for point, (velocityX, velocityY) in positionAndVelocity.items():
        point.setX(point.getX() + velocityX * stepSize)
        point.setY(point.getY() + velocityY * stepSize)

def calculateOptimalStartingTime(positionAndVelocity):
    result = 0
    times = 0
    for point, (velocityX, velocityY) in positionAndVelocity.items():
        if velocityX != 0 :
            result += abs(point.getX() / velocityX)
            times += 1
        if velocityY != 0 :
            result += abs(point.getY() / velocityY)
            times += 1
    return round(result / times)

def getManhattanDistance(positionAndVelocity):
    result = 0
    keysToCompareWith = list(positionAndVelocity.keys())
    for point in positionAndVelocity.keys():
        keysToCompareWith.remove(point)
        for point2 in keysToCompareWith:
            result += abs(point.getX() - point2.getX()) + abs(point.getY() - point2.getY())

    return result

def printList(positions):
    minX = 1000000
    minY = 1000000
    maxX = -1000000
    maxY = -1000000
    for point in positions:
        minX = min(minX, point.getX())
        minY = min(minY, point.getY())
        maxX = max(maxX, point.getX())
        maxY = max(maxY, point.getY())

    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            printed = False
            for point in positions:
                if point.getX() == x and point.getY() == y:
                    printed = True
                    print("#", end='')
                    break
            if not printed:
                print(" ", end='')
        print("")
    print("")
    print("===================================================================================================================================")
    print("")

if __name__ == '__main__':
    inputList = open('./input/Day_10.txt', 'r').read().split("\n")
    print(solve(inputList))
