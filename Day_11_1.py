import math

def solve(serialNumber):
    highestPower = 0
    highestX = 0
    highestY = 0
    powerDictionary = {}
    for x in range(1,301):
        for y in range(1,301):
            powerDictionary[x, y] = getPowerLevel(x, y, serialNumber)
            if x > 2 and y > 2:
                totalPower = 0
                for x1 in range(x-2, x+1):
                    for y1 in range(y-2, y+1):
                        totalPower += powerDictionary[x1, y1]
                if totalPower > highestPower:
                    highestPower = totalPower
                    highestX = x-2
                    highestY = y-2
    return str(highestX) + "," + str(highestY)

def getPowerLevel(x, y, serialNumber):
    id = x + 10
    powerLevel = id * y
    withSerialNo = powerLevel + serialNumber
    multiplied = withSerialNo * id
    hundredthDigit = math.floor(multiplied / 100) % 10
    return hundredthDigit - 5

if __name__ == '__main__':
    serialNumber = int(open('./input/Day_11.txt', 'r').read())
    print(solve(serialNumber))