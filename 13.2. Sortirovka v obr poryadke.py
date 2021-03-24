print("Сортировка в обратном порядке")
amount = int(input())
numbers = []
for i in range(amount):
    numbers.append(int(input()))
checker = 0
while checker < amount:
    for i in range(amount - 1):
        if numbers[i] < numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            checker = 0
        else:
            checker += 1
for i in range(amount):
    print(numbers[i])
