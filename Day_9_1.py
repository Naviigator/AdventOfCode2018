from collections import deque

def solve(playerCount, lastValue):
    scores = {}
    for player in range(0, playerCount):
        scores[player] = 0

    playedMarbles = deque([0])
    currentPlayer = 0
    for marbleId in range(1, lastValue + 1):
        if marbleId % 23 == 0:
            playedMarbles.rotate(7)
            scores[currentPlayer] += marbleId + playedMarbles.pop()
            playedMarbles.rotate(-1)
        else:
            playedMarbles.rotate(-1)
            playedMarbles.append(marbleId)

        currentPlayer = (currentPlayer + 1) % playerCount

    return max(scores.values())

if __name__ == '__main__':
    inputList = open('./input/Day_9.txt', 'r').read().split(" ")
    print(solve(int(inputList[0]), int(inputList[6])))
