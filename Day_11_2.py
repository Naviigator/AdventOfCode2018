import math
import time

def solve(serialNumber):
    highestPower = 0
    highestX = 0
    highestY = 0
    highestSize = 0
    powerDictionary = {}
    for x in range(1,301):
        for y in range(1,301):
            powerDictionary[x, y] = getPowerLevel(x, y, serialNumber)

    for x in range(1, 301):
        for y in range(1, 301):
            totalPower = 0
            for size in range(1, 301 - max(x, y)):
                for x1 in range(x, x + size):
                    totalPower += powerDictionary[x1, y + size - 1]
                for y1 in range(y, y + size - 1):
                    totalPower += powerDictionary[x + size - 1, y1]
                if totalPower > highestPower:
                    highestPower = totalPower
                    highestX = x
                    highestY = y
                    highestSize = size

    return str(highestX) + "," + str(highestY) + "," + str(highestSize)

def getPowerLevel(x, y, serialNumber):
    id = x + 10
    powerLevel = id * y
    withSerialNo = powerLevel + serialNumber
    multiplied = withSerialNo * id
    hundredthDigit = math.floor(multiplied / 100) % 10
    return hundredthDigit - 5

if __name__ == '__main__':
    serialNumber = int(open('./input/Day_11.txt', 'r').read())
    startTime = time.time()
    print(solve(serialNumber))
    print("--- %s seconds ---" % (time.time() - startTime))