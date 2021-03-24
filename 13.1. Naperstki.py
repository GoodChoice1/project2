print("Напёрстки")
amount = int(input())
items = [''] * amount
for i in range(amount):
    items[i] = input()
amount = int(input())
for i in range(amount):
    amountLeft = int(input())
    itemsTemp = [''] * amountLeft
    for j in range(amountLeft):
        number = int(input())
        for k in range(len(items)):
            if number == k + 1:
                itemsTemp[j] = items[k]
    items = itemsTemp.copy()
print(*items, sep='\n')
