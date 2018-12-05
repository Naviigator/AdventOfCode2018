def solve(challenge):
    smallestSize = 100000
    for charToRemove in char_range('a', 'z'):
        output = ""
        for c in challenge:
            previousChar = output[-1] if output != "" else None
            if isInversePolarity(c, previousChar):
                c = None
                output = output[0:-1]
            if c is not None and c.lower() == charToRemove:
                c = None
            if c is not None:
                output += c
        if len(output) < smallestSize:
            smallestSize = len(output)

    return smallestSize

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def isInversePolarity(c1, c2):
    return c1 is not None and c2 is not None and c1 != c2 and c1.upper() == c2.upper()

if __name__ == '__main__':
    suitComposition = open('./input/Day_5.txt', 'r').read()
    print(solve(suitComposition))
