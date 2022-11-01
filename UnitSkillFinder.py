file = open('UnitTypes.java', 'r')
lineList = file.readlines()
unitList = []
healthList = []

for i in range(len(lineList)):
    if 'health' in lineList[i]:
        nameFound = False
        index = i
        unit = ''
        while True:
            if 'UnitType' in lineList[index]:
                foundQuote = False
                for j in lineList[index]:
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
            index -= 1

        health = ''
        for j in lineList[i]:
            if j.isnumeric() is True:
                health += j
        healthList.append(int(health))