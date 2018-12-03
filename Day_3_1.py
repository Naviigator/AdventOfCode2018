def solve(fabricDefinitions):
    claimedFabric = {}
    for fabricDefinition in fabricDefinitions:
        if fabricDefinition != "":
            splitDefinition = fabricDefinition.split(" ")
            id = splitDefinition[0][1:]
            xAndY = splitDefinition[2].split(",")
            startingX = int(xAndY[0])
            startingY = int(xAndY[1].strip(":"))
            wAndH = splitDefinition[3].split("x")
            w = int(wAndH[0])
            h = int(wAndH[1])
            for x in range(startingX, startingX + w):
                for y in range(startingY, startingY + h):
                    location = (x,y)
                    if location not in claimedFabric:
                        claimedFabric[location] = 0
                    claimedFabric[location] += 1

    return len(list(filter(lambda x: x > 1, claimedFabric.values())))

if __name__ == '__main__':
    fabricDefinitions = open('./input/Day_3.txt', 'r').read().split("\n")
    fabricDefinitions = filter(lambda x: x != '', fabricDefinitions)
    print(solve(fabricDefinitions))
