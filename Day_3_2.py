def solve(fabricDefinitions):
    claimedFabric = {}
    for fabricDefinition in fabricDefinitions:
        if fabricDefinition != "":
            id, h, startingX, startingY, w = inputToVariables(fabricDefinition)
            for x in range(startingX, startingX + w):
                for y in range(startingY, startingY + h):
                    location = (x,y)
                    if location not in claimedFabric:
                        claimedFabric[location] = 0
                    claimedFabric[location] += 1


    for fabricDefinition in fabricDefinitions:
        if fabricDefinition != "":
            id, h, startingX, startingY, w = inputToVariables(fabricDefinition)
            if isValid(claimedFabric, h, startingX, startingY, w):
                return id
    return "none found..."


def isValid(claimedFabric, h, startingX, startingY, w):
    for x in range(startingX, startingX + w):
        for y in range(startingY, startingY + h):
            location = (x, y)
            if claimedFabric[location] != 1:
                return False
    return True


def inputToVariables(fabricDefinition):
    splitDefinition = fabricDefinition.split(" ")
    id = splitDefinition[0][1:]
    xAndY = splitDefinition[2].split(",")
    startingX = int(xAndY[0])
    startingY = int(xAndY[1].strip(":"))
    wAndH = splitDefinition[3].split("x")
    w = int(wAndH[0])
    h = int(wAndH[1])
    return id, h, startingX, startingY, w


if __name__ == '__main__':
    fabricDefinitions = open('./input/Day_3.txt', 'r').read().split("\n")
    fabricDefinitions = list(filter(lambda x: x != '', fabricDefinitions))
    print(solve(fabricDefinitions))
