def solve(coordinates):
    minX = 1000000
    minY = 1000000
    maxX = -1000000
    maxY = -1000000
    inputCoordinates = {}
    coordinatesWithManhattanDistance = {}
    id = 0
    for coordinate in coordinates:
        if coordinate == "":
            continue
        id += 1
        splitCoordinate = coordinate.split(",")
        x = int(splitCoordinate[0])
        y = int(splitCoordinate[1])
        coordinatesWithManhattanDistance[(x, y)] = id
        inputCoordinates[(x, y)] = id
        minX = min(minX, x)
        minY = min(minY, y)
        maxX = max(maxX, x)
        maxY = max(maxY, y)

    for x in range (minX, maxX + 1):
        for y in range(minY, maxY + 1):
            coordinatesWithManhattanDistance[x, y] = getManhattanClosestId(inputCoordinates, x, y)

    occurences = {}
    infiniteIds = findInfiniteIds(coordinatesWithManhattanDistance, minX, minY, maxX, maxY)
    for x in range (minX, maxX):
        for y in range (minY, maxY):
            foundId = coordinatesWithManhattanDistance[x, y]
            if foundId not in infiniteIds:
                if foundId not in occurences:
                    occurences[foundId] = 0
                occurences[foundId] += 1

    result = 0
    for value in occurences.values():
        result = max(result, value)
    return result


def findInfiniteIds(coordinatesWithManhattanDistance, minX, minY, maxX, maxY):
    infiniteIds = {None}
    for x in range(minX, maxX):
        infiniteIds.add(coordinatesWithManhattanDistance[x, minY])
        infiniteIds.add(coordinatesWithManhattanDistance[x, maxY])


    for y in range(minY, maxY):
        infiniteIds.add(coordinatesWithManhattanDistance[minX, y])
        infiniteIds.add(coordinatesWithManhattanDistance[maxX, y])

    return infiniteIds

def getManhattanClosestId(inputCoordinates, x, y):
    lowestDistance = None
    lowestDistanceId = None
    for coordX, coordY in inputCoordinates.keys():
        distance = abs(coordX - x) + abs(coordY - y)
        if lowestDistance is None or lowestDistance > distance:
            lowestDistance = distance
            lowestDistanceId = inputCoordinates[(coordX, coordY)]
        elif lowestDistance == distance:
            lowestDistanceId = None

    return lowestDistanceId

if __name__ == '__main__':
    coordinates = open('./input/Day_6.txt', 'r').read().split("\n")
    print(solve(coordinates))
