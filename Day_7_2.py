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

    links = dict(allLinks)
    done = False
    processingLinks = {}
    timeSpent = 0
    while not done:
        allChars = []
        lockedChars = []
        for probablyLockedChar, potentiallyUnlockedChars in links.items():
            if potentiallyUnlockedChars:
                lockedChars.append(probablyLockedChar)
            allChars.append(probablyLockedChar)
            for potentiallyUnlockedChar in potentiallyUnlockedChars:
                allChars.append(potentiallyUnlockedChar)

        firstChars = list(set([char for char in allChars if char not in lockedChars]))
        firstChars.sort()
        while len(processingLinks) < 5 and firstChars and not done:
            if firstChars:
                chosenChar = firstChars[0]
                del firstChars[0]
                if chosenChar not in processingLinks:
                    processingLinks[chosenChar] = getWorktimeFor(chosenChar)

        if not processingLinks:
            done = True

        if not done:
            timePassed = min(processingLinks.values())
            timeSpent += timePassed
            keysToDelete = []
            for key in processingLinks.keys():
                processingLinks[key] -= timePassed
                if processingLinks[key] <= 0:
                    keysToDelete.append(key)
                    for linkKey in links.keys():
                        links[linkKey] = [c for c in links[linkKey] if c != key]

                if key in links:
                    del links[key]
            for key in keysToDelete:
                del processingLinks[key]

    return timeSpent

def getWorktimeFor(c):
    return 60 + ord(c) - ord('A') + 1

if __name__ == '__main__':
    lines = open('./input/Day_7.txt', 'r').read().split("\n")
    lines = list(filter(lambda x: x != '', lines))
    print(solve(lines))
