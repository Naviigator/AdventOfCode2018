up = 0
right = 1
down = 2
left  = 3

nextIntersectLeft = -1
nextIntersectStraight = 0
nextIntersectRight = 1

railroadChars = ['|', '-', '/', '\\', '+', ' ']
coveringChars = {up: '|', right: '-', down: '|', left: '-'}
directions = {'^': up, '>': right, 'v': down, '<': left}
invertedDirections = {v: k for k, v in directions.items()}


def solve(trackState):
    trainId = 1
    map = {}
    trains = {}
    maxX = 0
    for line in trackState:
        maxX = max(maxX, len(line))

    for y in range(0, len(trackState)):
        line = trackState[y]
        for x in range(0, maxX):
            if x >= len(line):
                c = ' '
            else:
                c = line[x]

            if c in railroadChars:
                map[(x, y)] = c
            else:
                map[(x, y)] = chr(trainId)
                direction = directions[c]
                trains[trainId] = (direction, nextIntersectLeft, coveringChars[direction])
                trainId += 1


    while True:
        newMap = {}
        for y in range(0, len(trackState)):
            for x in range(0, maxX):
                c = map[(x, y)]
                if c in railroadChars:
                    if (x, y) not in newMap:
                        newMap[(x, y)] = c
                    continue

                id = ord(c)
                (direction, nextIntersectDirection, coveringChar) = trains[id]
                nextX, nextY = getNextXAndY(direction, x, y)

                nextChar = map[(nextX, nextY)]
                if (nextX, nextY) in newMap:
                    nextChar = newMap[(nextX, nextY)]
                    if nextChar not in railroadChars:
                        otherId = ord(nextChar)
                        (otherDirection, otherNextIntersectDirection, otherCoveringChar) = trains[otherId]
                        map[x, y] = coveringChar
                        map[nextX, nextY] = otherCoveringChar
                        newMap[x, y] = coveringChar
                        newMap[nextX, nextY] = otherCoveringChar
                        continue
                elif nextChar not in railroadChars:
                    otherId = ord(nextChar)
                    (otherDirection, otherNextIntersectDirection, otherCoveringChar) = trains[otherId]
                    map[x, y] = coveringChar
                    map[nextX, nextY] = otherCoveringChar
                    newMap[x, y] = coveringChar
                    newMap[nextX, nextY] = otherCoveringChar
                    continue


                direction, nextIntersectDirection = getNextDirectionAndIntersectDirection(direction, nextChar,
                                                                                          nextIntersectDirection)

                newMap[(x, y)] = coveringChar
                newMap[(nextX, nextY)] = c
                trains[id] = (direction, nextIntersectDirection, nextChar)

        count = 0
        onlyRemainingX = 0
        onlyRemainingY = 0
        for (x, y), c in newMap.items():
            if c not in railroadChars:
                count += 1
                onlyRemainingX = x
                onlyRemainingY = y

        if count == 1:
            return onlyRemainingX, onlyRemainingY

        #printMap(newMap, trains)
        #print("==========next===========")
        map = newMap

def printMap(map, trains):
    maxX = 0
    maxY = 0
    for (x, y) in map.keys():
        maxX = max(x, maxX)
        maxY = max(y, maxY)

    for y in range(0, maxY + 1):
        for x in range(0, maxX + 1):
            c = map[(x, y)]
            if c in railroadChars:
                print(c, end='')
            else:
                id = ord(c)
                (direction, nextIntersectDirection, coveringChar) = trains[id]
                print(invertedDirections[direction], end='')
        print('')


def getNextDirectionAndIntersectDirection(direction, nextChar, nextIntersectDirection):
    if nextChar == '+':
        direction = turn(direction, nextIntersectDirection)
        nextIntersectDirection = getNextDirection(nextIntersectDirection)
    elif nextChar == '\\':
        if direction == up:
            direction = left
        elif direction == right:
            direction = down
        elif direction == down:
            direction = right
        elif direction == left:
            direction = up
    elif nextChar == '/':
        if direction == up:
            direction = right
        elif direction == right:
            direction = up
        elif direction == down:
            direction = left
        elif direction == left:
            direction = down
    return direction, nextIntersectDirection


def getNextXAndY(direction, x, y):
    nextX = x
    nextY = y
    if direction == up:
        nextY -= 1
    elif direction == down:
        nextY += 1
    elif direction == left:
        nextX -= 1
    elif direction == right:
        nextX += 1
    return nextX, nextY


def turn(currentOrientation, direction):
    return (currentOrientation + direction + 4) % 4

def getNextDirection(currentDirection):
    if currentDirection == nextIntersectRight:
        return nextIntersectLeft
    return currentDirection + 1



if __name__ == '__main__':
    trackState = open('./input/Day_13.txt', 'r').read().split("\n")
    print(solve(trackState))