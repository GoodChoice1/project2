print("Вертикальная диаграмма")
text = input()
numbers = []
max = -9999
for i in range(len(text)):
    if i % 2 == 0:
        if max < int(text[i]):
            max = int(text[i])
        numbers.append(int(text[i]))
width = len(numbers) + 2
height = max + 2
sign = "*"
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1:
            print(sign, end='')
        elif j == 0 or j == width - 1:
            print(sign, end='')
        elif height - i <= numbers[j - 1]:
            print(sign, end='')
        else:
            print(' ', end='')
    print("")