def addr(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] + registry[paramB]
    return result


def addri(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] + paramB
    return result

def mulr(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] * registry[paramB]
    return result

def muli(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] * paramB
    return result

def banr(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] & registry[paramB]
    return result

def bani(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] & paramB
    return result

def borr(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] | registry[paramB]
    return result

def bori(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] | paramB
    return result

def setr(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA]
    return result

def seti(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = paramA
    return result

def gtir(registry, paramA, paramB, paramC):
    result = dict(registry)
    if paramA > registry[paramB]:
        result[paramC] = 1
    else:
        result[paramC] = 0
    return result

def gtri(registry, paramA, paramB, paramC):
    result = dict(registry)
    if registry[paramA] > paramB:
        result[paramC] = 1
    else:
        result[paramC] = 0
    return result

def gtrr(registry, paramA, paramB, paramC):
    result = dict(registry)
    if registry[paramA] > registry[paramB]:
        result[paramC] = 1
    else:
        result[paramC] = 0
    return result

def eqir(registry, paramA, paramB, paramC):
    result = dict(registry)
    if paramA == registry[paramB]:
        result[paramC] = 1
    else:
        result[paramC] = 0
    return result

def eqri(registry, paramA, paramB, paramC):
    result = dict(registry)
    if registry[paramA] == paramB:
        result[paramC] = 1
    else:
        result[paramC] = 0
    return result

def eqrr(registry, paramA, paramB, paramC):
    result = dict(registry)
    if registry[paramA] == registry[paramB]:
        result[paramC] = 1
    else:
        result[paramC] = 0
    return result

allOps = [addr, addri, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def solve(puzzle):
    result = 0
    emptyLines = 0

    inputRegistry = {}
    outputRegistry = {}
    command = None
    paramA = None
    paramB = None
    paramC = None

    opNumberList = {}
    for i in range(0, 16):
        opNumberList[i] = list(allOps)

    lineNumber = -1
    for line in puzzle:
        lineNumber += 1
        processingTime = False
        if line == "":
            emptyLines += 1
            if emptyLines > 1:
                break
            continue
        emptyLines = 0
        if line.startswith("Before: "):
            inputRegistry = readRegistry(line)
        elif line.startswith("After: "):
            outputRegistry = readRegistry(line)
            processingTime = True
        else:
            command, paramA, paramB, paramC = extractCommandWithParams(command, line, paramA, paramB, paramC)

        if processingTime:
            actualOps = []
            for op in opNumberList[command]:
                resultRegistry = op(inputRegistry, paramA, paramB, paramC)
                if resultRegistry == outputRegistry:
                    actualOps.append(op)
            opNumberList[command] = actualOps

    allIsValid = False

    operationViaNumber = {}

    while len(operationViaNumber) != 16:
        for opId, funcs in opNumberList.items():
            if len(funcs) == 1:
                operationViaNumber[opId] = funcs[0]

        #find keys that are unique to 1 op
        invertedOpList = {}
        for opId, funcs in opNumberList.items():
            if opId in operationViaNumber.keys():
                continue
            for func in funcs:
                if func in operationViaNumber.values():
                    continue
                if func not in invertedOpList:
                    invertedOpList[func] = []
                invertedOpList[func].append(opId)

        for func, opIds in invertedOpList.items():
            if len(opIds) == 1:
                operationViaNumber[opIds[0]] = func

    registry = readRegistry("[0,0,0,0]")
    for line in puzzle[lineNumber:]:
        if len(line) == 0:
            continue
        command, paramA, paramB, paramC = extractCommandWithParams(command, line, paramA, paramB, paramC)
        registry = operationViaNumber[command](registry, paramA, paramB, paramC)

    return registry[0]


def extractCommandWithParams(command, line, paramA, paramB, paramC):
    tmp = line.split(" ")
    command = int(tmp[0])
    paramA = int(tmp[1])
    paramB = int(tmp[2])
    paramC = int(tmp[3])
    return command, paramA, paramB, paramC


def readRegistry(line):
    registry = {}
    tmp = line[line.index('[') + 1:]
    index = 0
    for content in tmp.split(','):
        registry[index] = int(content.strip(']'))
        index += 1
    return registry

if __name__ == '__main__':
    puzzle = open('./input/Day_16.txt', 'r').read().split("\n")
    print(solve(puzzle))