print("CSV 2.0")
length=int(input())
text=[]
textNew=[]
for i in range(length):
    text.append(input())
length=int(input())
for i in range(length):
    number=input()
    number=number.split(",")
    first=int(number[0])
    second=int(number[1])
    textNew.append(text[first].split(",")[second])
for i in range(len(textNew)):
    print(textNew[i])