print("Белый список")
amountOfWhiteList=int(input())
whiteList=[]
whiteFinds=[]
for i in range(amountOfWhiteList):
    whiteList.append(input())
amountOfFinds=int(input())
for i in range(amountOfFinds):
    word=input()
    for j in range(amountOfWhiteList):
        if word==whiteList[j]:
            whiteFinds.append(word)
for i in range(len(whiteFinds)):
    print(whiteFinds[i])