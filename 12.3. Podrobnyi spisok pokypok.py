print("Подробный список покупок")
amountOfStrings=int(input())
buy=[]
amountBuy=[]
for i in range(amountOfStrings):
    buy.append(input())
    amountBuy.append(input())
while amountOfStrings>0 :
    amountOfStrings-=1
    print(buy[amountOfStrings],amountBuy[amountOfStrings])