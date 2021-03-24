print("Экономия")
amount = int(input())
table = [[-1] * amount for i in range(amount)]
for i in range(1, amount):
    text = input()
    for j in range(len(text.split())):
        table[i][j] = int(text.split()[j])
first = input()
second = int(first.split()[1])
first = int(first.split()[0])
minim = 999999
minTemp = -2
number = first
checker = 0
while checker < amount * amount + 1:
    for i in range(amount):
        if table[i][first] != -1 and table[i][first] < table[second][first]:
            for j in range(amount):
                if table[i][j] != -1:
                    minTemp = table[i][first] + table[j][i]
                    if minTemp < minim:
                        minim = minTemp
                        number = i
    checker += 1
print(number)
