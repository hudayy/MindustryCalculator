# Initializes everything
file = open('UnitTypes.java', 'r')
lineList = file.readlines()
unitReader = False
unitList = []
speedList = []
hitSizeList = []
healthList = []

# Reads code line by line
for i in range(len(lineList)):
    #Adds all units to unitList
    if 'new UnitType' in lineList[i]:
        unitReader = True
        unit = ''
        for j in lineList[i]:
            if j.isalpha():
                unit += j
            elif unit == '': continue
            else: break
        unitList.append(unit)
    
    # Collecting Information
    if 'new Weapon' in lineList[i]:
        unitReader = False
    if unitReader:

        #Add all units' speed to speedList
        if 'speed' in lineList[i]:
            speed = ''
            for j in lineList[i]:
                if j.isnumeric():
                    speed += j
            speedList.append(float(speed))
            if len(speedList) < len(unitList): speedList.append(0.0)

        # Adds all units' hitSize to hitSizeList
        if 'hitSize' in lineList[i]:
            hitSize = ''
            for j in lineList[i]:
                if j.isnumeric() or j == '.':
                    hitSize += j
            hitSizeList.append(float(hitSize))
            if len(hitSizeList) < len(unitList): hitSizeList.append(0.0)

        # Adds all units' health to healthList
        if 'health' in lineList[i]:
            health = ''
            for j in lineList[i]:
                if j.isnumeric():
                    health += j
            healthList.append(float(health))
            if len(healthList) < len(unitList): healthList.append(0.0)
file.flush()
file.close()