print("Тотальная децимация")
amount=int(input())
names=[]
for i in range(amount):
    names.append(input())
killNumber=int(input())
while len(names)>0:
    killNumbers = []
    for i in range(len(names)):
        if i==0 or i % killNumber==0 :
            killNumbers.append(i)
    for i in range(len(killNumbers)):
        print(names[killNumbers[i]-i])
        names.pop(killNumbers[i]-i)


