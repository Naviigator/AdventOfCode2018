def commonCharacters(x, y):
    result = ""
    for i in range (0, len(x)):
        charX = x[i]
        charY = y[i]
        if charX == charY:
            result += charX

    return result

def almostEquals(x, y):
    return len(commonCharacters(x, y)) == len(x) - 1

def solve(serialNumbers):
    for i in range (0, len(serialNumbers)):
        serialNumber = serialNumbers[i]
        otherSerials = serialNumbers[i:]
        for otherSerial in otherSerials:
            if almostEquals(serialNumber, otherSerial):
                return commonCharacters(serialNumber, otherSerial)
    return "No matches..."


if __name__ == '__main__':
    serialNumbers = open('./input/Day_2.txt', 'r').read().split("\n")
    serialNumbers = list(filter(lambda x: x != '', serialNumbers))
    print(solve(serialNumbers))
