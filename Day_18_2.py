import math

GROUND = "."
TREE = "|"
LUMBERYARD = "#"
EMPTY = ""
NEIGHBOUR_POSITIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def solve(puzzle):
    land = {}
    y = -1
    x = None
    for line in puzzle:
        y += 1
        x = -1
        for c in line:
            x += 1
            land[(x, y)] = c

    printMap(land, x, y)
    time = 1000000000
    patternList = [land]
    patternFound = False
    i = 0
    while i < time:
        i += 1
        land = tick(land, x, y)
        if not patternFound and land in patternList:
            patternFound = True
            difference = len(patternList) - patternList.index(land)
            remainingTime = time - i
            i += math.floor(remainingTime / difference) * difference

        patternList.append(land)
        printMap(land, x, y)

    result = list(land.values())
    return result.count(TREE) * result.count(LUMBERYARD)

def tick(land, maxX, maxY):
    newMap = {}
    for y in range(0, maxY + 1):
        for x in range(0, maxX + 1):
            neighbours = []
            for position in NEIGHBOUR_POSITIONS:
                neighbours.append(get(land, x + position[0], y + position[1]))

            current = get(land, x, y)
            next = current
            if current == GROUND:
                if neighbours.count(TREE) > 2:
                    next = TREE
            elif current == TREE:
                if neighbours.count(LUMBERYARD) > 2:
                    next = LUMBERYARD
            elif current == LUMBERYARD:
                if neighbours.count(TREE) < 1 or neighbours.count(LUMBERYARD) < 1:
                    next = GROUND

            newMap[(x, y)] = next

    return newMap

def get(land, x, y):
    if (x, y) in land:
        return land[(x, y)]
    return EMPTY

def printMap(land, maxX, maxY):
    for y in range(0, maxY + 1):
        for x in range(0, maxX + 1):
            print(land[(x, y)], end = "")
        print()
    print()
    print()

if __name__ == '__main__':
    puzzle = open('./input/Day_18.txt', 'r').read().split("\n")
    print(solve(puzzle))