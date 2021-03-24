print("Дни рождения - 2")
length = int(input())
boys = []
answer = []
for i in range(length):
    boys.append(input())
length = int(input())
for i in range(length):
    month = input()
    answerTemp = ''
    for j in range(len(boys)):
        if month == boys[j].split()[2]:
            answerTemp += boys[j].split()[0] + " " + boys[j].split()[1] + " "
    answer.append(answerTemp)
for i in range(len(answer)):
    print(answer[i])