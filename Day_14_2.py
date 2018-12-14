import time

def solve(count):
    recipeBook = "37"
    indexes = [0, 1]
    while count not in recipeBook[-len(count) - 1:]:
        indexesToMove = []
        for index in indexes:
            number = int(recipeBook[index])
            indexesToMove.append(number)
        recipeBook += str(sum(indexesToMove))
        for j in range(0, len(indexes)):
            indexes[j] = (indexes[j] + 1 + indexesToMove[j]) % len(recipeBook)

    return recipeBook.index(count)

if __name__ == '__main__':
    count = open('./input/Day_14.txt', 'r').read()
    startTime = time.time()
    print(solve(count))
    print("--- %s seconds ---" % (time.time() - startTime))