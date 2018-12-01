currentValue = 0
challenges = open("./input/Day_1.txt").read().split("\n")
for challenge in challenges:
    challenge = challenge.strip(" ")
    if challenge != "":
        operator = challenge[0]
        numericValue = int(challenge[1:])
        if operator == '+':
            currentValue += numericValue
        elif operator == '-':
            currentValue -= numericValue
print(currentValue)
