print("Парадоксы статистики")
amount = int(input())
text = []
mediani = []
modi = []
fullString = ''
for i in range(amount):
    text.append(input())
for i in range(len(text)):
    fullString += " " + text[i]
    mediani.append(text[i].split()[len((text[i].split())) // 2])
    sign = 0
    signTemp = 0
    numberTemp = 0
    numberMax = 0
    for j in range(len(text[i].split())):
        signTemp = text[i].split()[j]
        numberTemp = 0
        for k in range(len(text[i].split())):
            if text[i].split()[j] == text[i].split()[k]:
                if numberTemp == 0:
                    numberTemp += 2
                else:
                    numberTemp += 1
        if numberTemp > numberMax:
            numberMax = numberTemp
            sign = signTemp
    modi.append(sign)
for i in range(len(mediani)):
    print(mediani[i], ' ', end='')
print('')
for i in range(len(modi)):
    print(modi[i], ' ', end='')
print('')
print(mediani[len(mediani) // 2])
numberMax = -9999
for i in range(len(modi)):
    signTemp = modi[i]
    numberTemp = 0
    for j in range(len(modi)):
        if modi[i] == modi[j]:
            numberTemp += 1
    if numberMax < numberTemp:
        sign = signTemp
        numberMax = numberTemp
print(sign)
print(fullString[len(fullString) // 2])
numberMax = -9999
for i in range(len(fullString.split())):
    signTemp = fullString.split()[i]
    numberTemp = 0
    for j in range(len(fullString.split())):
        if fullString.split()[i] == fullString.split()[j]:
            numberTemp += 1
    if numberMax < numberTemp:
        sign = signTemp
        numberMax = numberTemp
print(sign)
