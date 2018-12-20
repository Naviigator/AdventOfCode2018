def addr(registry, paramA, paramB, paramC):
    result = dict(registry)
    result[paramC] = registry[paramA] + registry[paramB]
    return result

def addi(registry, paramA, paramB, paramC):
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

allOps = {"addr": addr, "addi": addi, "mulr": mulr, "muli": muli, "banr": banr, "bani": bani, "borr": borr, "bori": bori, "setr": setr, "seti": seti, "gtir": gtir, "gtri": gtri, "gtrr": gtrr, "eqir": eqir, "eqri": eqri, "eqrr": eqrr}

def solve(puzzle):

    ipCommandSplit = puzzle[0].split(" ")
    registryToExecute = int(ipCommandSplit[1])

    actualPuzzle = puzzle[1:]

    registry = readRegistry("[0,0,0,0,0,0]")
    while True:
        ptr = registry[registryToExecute]
        if ptr < 0 or len(actualPuzzle) <= ptr:
            return registry[0]

        command, paramA, paramB, paramC = extractCommandWithParams(actualPuzzle[ptr])
        registry = allOps[command](registry, paramA, paramB, paramC)
        registry[registryToExecute] += 1


def extractCommandWithParams(line):
    tmp = line.split(" ")
    command = tmp[0]
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
    puzzle = open('./input/Day_19.txt', 'r').read().split("\n")
    print(solve(puzzle))