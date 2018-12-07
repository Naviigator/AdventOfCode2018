def solve(lines):
    allLinks = {}
    for line in lines:
        text = line.split(" ")
        stepToFinishFirst = text[1]
        stepToFinishLater = text[7]

        if stepToFinishLater not in allLinks:
            allLinks[stepToFinishLater] = {stepToFinishFirst}
        else:
            allLinks[stepToFinishLater].add(stepToFinishFirst)

    result = ""
    links = dict(allLinks)
    done = False
    while not done:
        allChars = []
        lockedChars = []
        for probablyLockedChar, potentiallyUnlockedChars in links.items():
            if potentiallyUnlockedChars:
                lockedChars.append(probablyLockedChar)
            allChars.append(probablyLockedChar)
            for potentiallyUnlockedChar in potentiallyUnlockedChars:
                allChars.append(potentiallyUnlockedChar)

        firstChars = [char for char in allChars if char not in lockedChars]
        if firstChars:
            firstChars.sort()
            chosenChar = firstChars[0]
            result += chosenChar
            for key in links.keys():
                links[key] = [c for c in links[key] if c != chosenChar]

            if chosenChar in links:
                del links[chosenChar]
        else:
            done = True

    return result

if __name__ == '__main__':
    lines = open('./input/Day_7.txt', 'r').read().split("\n")
    lines = list(filter(lambda x: x != '', lines))
    print(solve(lines))
