print("Минификатор")
amount = int(input())
text = []
for i in range(amount):
    word = input()
    trueWord = ''
    isInPrint = False
    previousChar = ''
    if word[0] == ' ':
        isFirstSpace = True
    else:
        isFirstSpace = False
    for j in word:
        if j == "'" and not isInPrint:
            isInPrint = True
        elif j == "'" and isInPrint and previousChar != "\\":
            isInPrint = False
        if j != ' ' and previousChar == ' ':
            isFirstSpace = False
            trueWord += j
        elif j == ' ' and isFirstSpace and not isInPrint:
            trueWord += j
        elif j == '#' and not isInPrint:
            break
        elif j == ' ' and previousChar == ' ':
            pass
        else:
            trueWord += j
        previousChar = j
    text.append(trueWord)
for i in text:
    print(i)
