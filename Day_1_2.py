result = None
currentValue = 0
values_hit = {0}
challenges = open("./input/Day_1.txt").read().split("\n")
while result is None:
    for challenge in challenges:
        challenge = challenge.strip(" ")
        if challenge != "":
            operator = challenge[0]
            numericValue = int(challenge[1:])
            if operator == '+':
                currentValue += numericValue
            elif operator == '-':
                currentValue -= numericValue

            if currentValue in values_hit:
                result = currentValue
                break
            values_hit.add(currentValue)
print(result)
