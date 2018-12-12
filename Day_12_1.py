def solve(state, rulesList):
    index = 0
    rules = {}
    for rule in rulesList:
        splitRule = rule.split(" => ")
        rules[splitRule[0]] = splitRule[1]
    defaultPot = "."
    loopTimes = 20
    for i in range(0,loopTimes):
        newState = ".."

        firstFilledPot = state.index("#")
        state = defaultPot + defaultPot + defaultPot + defaultPot + state.strip(".") + defaultPot + defaultPot + defaultPot + defaultPot
        index += firstFilledPot - 4

        for j in range(2, len(state) - 1):
            sliceToCheck = state[j-2:j+3]
            if sliceToCheck in rules:
                newState += rules[sliceToCheck]
            else:
                newState += "."
        state =  newState

    return calcSum(state, index)

def calcSum(state, index):
    result = 0
    for char in state:
        if char == "#":
            result += index
        index += 1
    return result

if __name__ == '__main__':
    inp = open('./input/Day_12.txt', 'r').read().split("\n")
    print(solve(inp[0][15:], inp[2:]))