print("Два пути")
amount = int(input())
statFirst = []
statSecond = []
for i in range(amount):
    x=int(input())
    statFirst.append(x)
    statSecond.append(x)
amount = int(input())
for i in range(amount):
    numberBro = int(input())
    numberStat = int(input())
    statGain = int(input())
    if numberBro == 1:
        statFirst[numberStat] += statGain
    elif numberBro == 2:
        statSecond[numberStat] += statGain
checker = 0
for i in range(len(statFirst)):
    print(statFirst[i], end=" ")
print("")
for i in range(len(statSecond)):
    print(statSecond[i], end=" ")
    if statFirst[i] == statSecond[i]:
        checker += 1
print("")
print(checker)
