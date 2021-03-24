print("Проверка чека")
text = input()
amountOfPositions = int(text[0:3])
sumPrice = int(text[3:len(text)])
wrongPositions = []
wrongPrice = 0
isWrong = False
for i in range(amountOfPositions):
    text = input()
    price = int(text[0:6])
    amount = int(text[8:12])
    priceEnd = int(text[13:len(text)])
    checkSum = price * amount
    sumPrice -= checkSum
    if checkSum != priceEnd:
        isWrong = True
        wrongPositions.append(i + 1)
print(sumPrice)
if isWrong:
    for i in range(len(wrongPositions)):
        print(wrongPositions[i], end= " ")
