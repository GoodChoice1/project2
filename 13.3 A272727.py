print("А272727")
length = int(input()) - 1
numbers = []
numbers.append(0)
start = 0
end = 0
for i in range(length):
    start = 0
    end = len(numbers) - 1
    checker = 0
    while end != -1:
        if numbers[start] == numbers[end]:
            checker += 1
        start += 1
        end -= 1
    numbers.append(checker)
length += 1
for i in range(length):
    print(numbers[i])
