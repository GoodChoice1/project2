print("Права доступа")
amount = int(input())
accessList = []
answers = []
for i in range(amount):
    accessList.append(input())
amount = int(input())
for i in range(amount):
    text = input()
    isAcessable = False
    for j in range(len(accessList)):
        if len(accessList[j].split('/')) <= len(text.split('/')) and not isAcessable:
            checker = 0
            for k in range(len(accessList[j].split('/'))):
                if accessList[j].split('/')[k] == text.split('/')[k]:
                    checker += 1
            if checker == len(text.split('/')) - 1:
                isAcessable = True
    if isAcessable:
        answers.append('YES')
    else:
        answers.append('NO')
print(*answers, sep='\n')
