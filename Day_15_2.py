up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
allDirections = [up, left, right, down]
allDirectionsIncludingNone = [None, up, left, right, down]

class Creature:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.damage = 3
        self.hp = 200

    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x

class TraversablePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.traversed = False
        self.reachedViaFirstGoing = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def solve(mapList):
    initialCreatures = []
    initialMap = {}

    for y in range(0, len(mapList)):
        currentRow = mapList[y]
        for x in range(0, len(currentRow)):
            c = currentRow[x]
            initialMap[(x, y)] = c
            if c != "#" and c != ".":
                initialCreatures.append(Creature(c, x, y))

    initialElvenCreatures = len(list(filter(lambda critter: critter.type == "E", initialCreatures)))
    initialMap = initialMap
    elvenDamage = 3
    while True:
        elvenDamage += 1
        creatures = []
        map = dict(initialMap)
        for creature in initialCreatures:
            newCreature = Creature(creature.type, creature.x, creature.y)
            if newCreature.type == "E":
                newCreature.damage = elvenDamage
            creatures.append(newCreature)
        combatFinished = False
        roundCount = 0
        while not combatFinished:
            someCreaturesSkipped = False
            creatures.sort()
            for creature in creatures:
                if combatFinished:
                    someCreaturesSkipped = True
                    continue
                if creature.hp <= 0:
                    continue

                enemyType = "G"
                if creature.type == "G":
                    enemyType = 'E'
                enemies = list(filter(lambda critter: critter.type == enemyType and critter.hp > 0, creatures))

                legalPoints = set()
                for enemy in enemies:
                    for (x, y) in allDirections:
                        position = (enemy.x + x, enemy.y + y)
                        if position in map and map[position] == '.' or (creature.x, creature.y) == position:
                            legalPoints.add(TraversablePoint(*position))

                    enemyPoint = TraversablePoint(enemy.x, enemy.y)
                    enemyPoint.traversed = True
                    legalPoints.add(enemyPoint)

                newLegalPoints = legalPoints
                legalPoints = {}
                while legalPoints != newLegalPoints and not creatureCanMoveTo(creature, newLegalPoints):
                    legalPoints = set(newLegalPoints)#copy for iteration
                    for possiblyTraversedPoint in legalPoints:
                        if not possiblyTraversedPoint.traversed:
                            for (x, y) in allDirections:
                                position = (possiblyTraversedPoint.x + x, possiblyTraversedPoint.y + y)
                                if position in map and map[position] == '.':

                                    point = TraversablePoint(*position)
                                    point.reachedViaFirstGoing = possiblyTraversedPoint.reachedViaFirstGoing
                                    if point.reachedViaFirstGoing is None:
                                        point.reachedViaFirstGoing = (x, y)

                                    newLegalPoints.add(point)
                            possiblyTraversedPoint.traversed = True

                moveCreature(creature, newLegalPoints, map)
                attack(creature, enemies, map)
                combatFinished = len(list(filter(lambda critter: critter.type == "G" and critter.hp > 0, creatures))) == 0 \
                                 or len(list(filter(lambda critter: critter.type == "E" and critter.hp > 0, creatures))) == 0

            creatures = list(filter(lambda critter: critter.hp > 0, creatures))
            if not someCreaturesSkipped:
                roundCount += 1

        if len(list(filter(lambda critter: critter.type == "E", creatures))) == initialElvenCreatures:
            healthLeft = 0
            for creature in creatures:
                healthLeft += creature.hp
            return roundCount * healthLeft


def attack(creature, enemies, map):
    currentEnemy = Creature("Dummy", 0, 0)
    currentEnemy.hp = 201
    for chosenDirection in allDirections:
        possibleX = creature.x + chosenDirection[0]
        possibleY = creature.y + chosenDirection[1]
        for enemy in enemies:
            if enemy.x == possibleX and enemy.y == possibleY and enemy.hp < currentEnemy.hp:
                currentEnemy = enemy

    currentEnemy.hp -= creature.damage
    if currentEnemy.hp <= 0:
        map[(currentEnemy.x, currentEnemy.y)] = '.'

def moveCreature(creature, legalPoints, map):
    for chosenDirection in allDirectionsIncludingNone:
        x = creature.x
        y = creature.y
        if chosenDirection is not None:
            x += chosenDirection[0]
            y += chosenDirection[1]
        if TraversablePoint(x, y) in legalPoints:
            if chosenDirection is not None:
                map[(creature.x, creature.y)] = '.'
                creature.x = x
                creature.y = y
                map[(creature.x, creature.y)] = creature.type
            return


def creatureCanMoveTo(creature, points):
    for direction in allDirectionsIncludingNone:
        x = creature.x
        y = creature.y
        if direction is not None:
            x += direction[0]
            y += direction[1]
        if TraversablePoint(x, y) in points:
            return True

    return False

if __name__ == '__main__':
    map = open('./input/Day_15.txt', 'r').read().split("\n")
    print(solve(map))