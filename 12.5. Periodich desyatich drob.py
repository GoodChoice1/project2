print("Периодическая десятичная дробь")
number = int(input())
leftNumber = 1
dividers = []
remainder = []
answer = ''
while leftNumber not in dividers:
    dividers.append(leftNumber)
    remainder.append(leftNumber * 10 // number)
    leftNumber = (leftNumber * 10) % number
for i in remainder[dividers.index(leftNumber):]:
    answer += str(i)
print(answer)
