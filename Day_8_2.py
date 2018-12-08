class Node:
    def __init__(self, list):
        childCount = list[0]
        metadataCount = list[1]
        self.children = []

        index = 2
        for childIndex in range(0, childCount):
            child = Node(list[index:])
            self.children.append(child)
            index += child.size()

        self.metadata = list[index:index+metadataCount]

    def size(self):
        size = 0
        for child in self.children:
            size += child.size()
        return size + 2 + len(self.metadata)

    def getMetadataValue(self):
        if self.children:
            result = 0
            for metadata in self.metadata:
                index = metadata -1
                if index < len(self.children):
                    result += self.children[index].getMetadataValue()
            return result
        return sum(self.metadata)

def solve(licenseList):
    rootNode = Node(licenseList)

    return rootNode.getMetadataValue()

if __name__ == '__main__':
    licenseList = open('./input/Day_8.txt', 'r').read().split(" ")
    print(solve([int(x) for x in licenseList]))
