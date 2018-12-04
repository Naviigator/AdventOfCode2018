def solve(guardLog):
    sleepTimePerGuard = {}
    totalSleeptimePerGuard = {}
    currentGuard = -1
    asleepSince = None
    for guardEntry in guardLog:
        if guardEntry != "":
            hours, minutes, payload = inputToVariables(guardEntry)
            if payload[0] == "Guard":
                currentGuard = int(payload[1].strip("#"))
            elif payload[0] == "falls":
                asleepSince = minutes
            elif payload[0] == "wakes":
                if asleepSince is None:
                    return "Something went horribly wrong!"
                if currentGuard not in sleepTimePerGuard:
                    totalSleeptimePerGuard[currentGuard] = 0
                    sleepTimePerGuard[currentGuard] = {}
                    for initializeMinute in range (0, 60):
                        sleepTimePerGuard[currentGuard][initializeMinute] = 0
                for sleepyMinute in range(asleepSince, minutes):
                    totalSleeptimePerGuard[currentGuard] += 1
                    sleepTimePerGuard[currentGuard][sleepyMinute] += 1

    mostSleepyGuard = -1
    mostSleepTime = 0
    for guardId, sleepyTime in totalSleeptimePerGuard.items():
        if sleepyTime > mostSleepTime:
            mostSleepTime = sleepyTime
            mostSleepyGuard = guardId

    mostSleepyMinute = -1
    mostSleepTimePerMinute = -1
    for sleepyMinute, asleepOnThatMinute in sleepTimePerGuard[mostSleepyGuard].items():
        if asleepOnThatMinute > mostSleepTimePerMinute:
            mostSleepyMinute = sleepyMinute
            mostSleepTimePerMinute = asleepOnThatMinute
    return mostSleepyGuard * mostSleepyMinute


def isValid(claimedFabric, h, startingX, startingY, w):
    for x in range(startingX, startingX + w):
        for y in range(startingY, startingY + h):
            location = (x, y)
            if claimedFabric[location] != 1:
                return False
    return True


def inputToVariables(guardEntry):
    splitEntry = guardEntry.split(" ")
    hoursAndMinutes = splitEntry[1].strip("]").split(":")
    hours = int(hoursAndMinutes[0])
    minutes = int(hoursAndMinutes[1])
    payload = splitEntry[2:]
    return hours, minutes, payload


if __name__ == '__main__':
    guardLog = open('./input/Day_4.txt', 'r').read().split("\n")
    guardLog = list(filter(lambda x: x != '', guardLog))
    guardLog.sort()
    print(solve(guardLog))
