def solve(serialNumbers):
    duplicatesCount = {}
    for serialNumber in serialNumbers:
        letterCount = {}
        for character in serialNumber:
            if character not in letterCount:
                letterCount[character] = 0
            letterCount[character] += 1



        for currentVal in set(letterCount.values()):
            if  currentVal > 1:
                if currentVal not in duplicatesCount:
                    duplicatesCount[currentVal] = 0
                duplicatesCount[currentVal] += 1

    return duplicatesCount[2] * duplicatesCount[3]

if __name__ == '__main__':
    serialNumbers = open('./input/Day_2.txt', 'r').read().split("\n")
    serialNumbers = filter(lambda x: x != '', serialNumbers)
    print(solve(serialNumbers))
