def solve(coordinates):
    minX = 1000000
    minY = 1000000
    maxX = -1000000
    maxY = -1000000
    inputCoordinates = {}
    id = 0
    for coordinate in coordinates:
        if coordinate == "":
            continue
        id += 1
        splitCoordinate = coordinate.split(",")
        x = int(splitCoordinate[0])
        y = int(splitCoordinate[1])
        inputCoordinates[(x, y)] = id
        minX = min(minX, x)
        minY = min(minY, y)
        maxX = max(maxX, x)
        maxY = max(maxY, y)

    validCoordinates = 0
    for x in range (minX, maxX + 1):
        for y in range(minY, maxY + 1):
            if isManhattanDistanceValid(inputCoordinates, x, y):
                validCoordinates += 1

    return validCoordinates

def isManhattanDistanceValid(inputCoordinates, x, y):
    distance = 0
    for coordX, coordY in inputCoordinates.keys():
        distance += abs(coordX - x) + abs(coordY - y)

    return distance < 10000

if __name__ == '__main__':
    coordinates = open('./input/Day_6.txt', 'r').read().split("\n")
    print(solve(coordinates))
