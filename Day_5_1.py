def solve(challenge):
    output = ""
    for c in challenge:
        previousChar = output[-1] if output != "" else None
        if isInversePolarity(c, previousChar):
            c = None
            output = output[0:-1]
        if c is not None:
            output += c

    return output


def isInversePolarity(c1, c2):
    return c1 is not None and c2 is not None and c1 != c2 and c1.upper() == c2.upper()

if __name__ == '__main__':
    suitComposition = open('./input/Day_5.txt', 'r').read()
    print(len(solve(suitComposition)))
