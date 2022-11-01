# Initializes Everything
file = open('UnitTypes.java', 'r')
lineList = file.readlines()
unitList = []
healthList = []

# Reads code line by line
for i in range(len(lineList)):
    # Adds all units to unitList
    if 'new UnitType' in lineList[i]:
        nameFound = False
        unit = ''
        while True:
            foundQuote = False
            for j in lineList[i]:
                if foundQuote is True:
                    if j.isalpha() is True:
                        unit += j
                else:
                    if j == '\"':
                        foundQuote = True
                    else:
                        continue
            unitList.append(unit)
            break

    # Adds all units' health to healthList
    if 'health' in lineList[i]:
        health = ''
        for j in lineList[i]:
            if j.isnumeric() is True:
                health += j
        healthList.append(int(health))

# Puts everything into a dictionary
troopDict = {unitList[i]: healthList[i] for i in range(len(unitList))}
print(troopDict)