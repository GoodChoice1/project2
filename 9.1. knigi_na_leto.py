print("Книги на лето")
firstAmount=int(input())
secondAmount=int(input())
first = []
second = []
for i in range (firstAmount):
    first.append(input())
for i in range(secondAmount):
    second.append(input())
for i in range(secondAmount):
    check = False
    for k in range(firstAmount):
        if second[i]==first[k]:
            check=True
    if check:
        print("YES")
    else:
        print("NO")