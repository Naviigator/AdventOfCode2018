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
    for line in puzzle:
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
            tmp = line.split(" ")
            command = tmp[0]
            paramA = int(tmp[1])
            paramB = int(tmp[2])
            paramC = int(tmp[3])

        if processingTime:
            potentialOpCount = 0
            for op in allOps:
                resultRegistry = op(inputRegistry, paramA, paramB, paramC)
                if resultRegistry == outputRegistry:
                    potentialOpCount += 1
            if potentialOpCount > 2:
                result += 1


    return result

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