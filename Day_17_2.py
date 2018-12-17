CLAY = "#"
SPRING = "+"
SAND = " "
FLOWING_WATER = "|"
STILL_WATER = "~"

def solve(puzzle):
    actualMap = {}
    minX = 500
    maxX = 500
    minY = 100000
    maxY = 0

    for line in puzzle:
        xAndY = line.split(",")
        fixedCoord = int(xAndY[0][2:])
        coordListString = xAndY[1][3:]
        coordList = coordListString.split("..")
        coordMin = int(coordList[0])
        coordMax = int(coordList[1])
        for dynamicCoord in range(coordMin, coordMax + 1):
            x = dynamicCoord
            y = fixedCoord
            if line.startswith("x"):
                x = fixedCoord
                y = dynamicCoord

            maxX = max(maxX, x)
            minX = min(minX, x)
            maxY = max(maxY, y)
            minY = min(minY, y)
            actualMap[(x, y)] = "#"

    waterMap = {}
    coordinates = (500, minY)
    if coordinates in actualMap and actualMap[coordinates] == CLAY:
        return "Could not start the water flow and I was too lazy to implement a way that's smarter."
    else:
        actualMap[coordinates] = FLOWING_WATER
        waterMap = {coordinates}

    #we want a buffer of sand to the left and the right
    maxX += 1
    minX -= 1
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            coordinates = (x, y)
            if coordinates not in actualMap:
                actualMap[coordinates] = SAND

    while len(waterMap) != 0:
        waterMap = tick(actualMap, waterMap, maxX)

    printMap(actualMap, minX, minY, maxX, maxY)
    return len(list(filter(lambda c: c == STILL_WATER, actualMap.values())))


def tick(actualMap, waterMap, maxX):
    nextWaterSet = set()
    for (x, y) in waterMap:
        coordinates = (x, y + 1)
        if coordinates in actualMap:
            if actualMap[coordinates] == SAND:
                nextWaterSet.add(coordinates)
                actualMap[coordinates] = FLOWING_WATER
            elif actualMap[coordinates] == STILL_WATER or actualMap[coordinates] == CLAY:
                newCoordinatesList = [(x - 1, y), (x + 1, y)]
                for newCoordinates in newCoordinatesList:
                    if newCoordinates not in actualMap:
                        continue
                    if actualMap[newCoordinates] == SAND:
                        nextWaterSet.add(newCoordinates)
                        actualMap[newCoordinates] = FLOWING_WATER
                    elif actualMap[newCoordinates] == CLAY or actualMap[newCoordinates] == FLOWING_WATER:
                        ranges = [range(x, 0, -1), range(x, maxX + 1)]

                        wallIndexes = []
                        for currentRange in ranges:
                            for checkX in currentRange:
                                if actualMap[(checkX, y)] == CLAY:
                                    wallIndexes.append(checkX)
                                    break
                                elif actualMap[(checkX, y)] != FLOWING_WATER:
                                    break

                        if len(wallIndexes) == 2:
                            firstWaterIndex = min(wallIndexes) + 1
                            for changeX in range(firstWaterIndex, max(wallIndexes)):
                                if actualMap[(changeX, y)] == FLOWING_WATER:
                                    actualMap[(changeX, y)] = STILL_WATER
                                    if actualMap[(changeX, y - 1)] == FLOWING_WATER:
                                        nextWaterSet.add((changeX, y - 1))
                                else:
                                    break

    return nextWaterSet


def printMap(map, minX, minY, maxX, maxY):
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            print(map[(x, y)], end = "")
        print()
    print()
    print()

if __name__ == '__main__':
    puzzle = open('./input/Day_17.txt', 'r').read().split("\n")
    print(solve(puzzle))