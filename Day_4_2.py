def solve(guardLog):
    sleepTimePerGuard = {}
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
                    sleepTimePerGuard[currentGuard] = {}
                    for initializeMinute in range (0, 60):
                        sleepTimePerGuard[currentGuard][initializeMinute] = 0
                for sleepyMinute in range(asleepSince, minutes):
                    sleepTimePerGuard[currentGuard][sleepyMinute] += 1

    mostSleepyGuard = -1
    mostSleepyMinute = -1
    mostSleepTimePerMinute = -1
    for currentGuard in sleepTimePerGuard.keys():
        for sleepyMinute, asleepOnThatMinute in sleepTimePerGuard[currentGuard].items():
            if asleepOnThatMinute > mostSleepTimePerMinute:
                mostSleepyGuard = currentGuard
                mostSleepyMinute = sleepyMinute
                mostSleepTimePerMinute = asleepOnThatMinute
    return mostSleepyGuard * mostSleepyMinute

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
