def solve(count):
    recipeBook = "37"
    indexes = [0, 1]
    endResultCount = 10
    while len(recipeBook) < count + endResultCount:
        indexesToMove = []
        for index in indexes:
            number = int(recipeBook[index])
            indexesToMove.append(number)
        recipeBook += str(sum(indexesToMove))
        for j in range(0, len(indexes)):
            indexes[j] = (indexes[j] + 1 + indexesToMove[j]) % len(recipeBook)

    return recipeBook[count : count + endResultCount]

if __name__ == '__main__':
    count = int(open('./input/Day_14.txt', 'r').read())
    print(solve(count))