print("Фильтр")
amount = int(input())
text = []
for i in range(amount):
    word = input()
    if word[0] == '%' and word[1] == '%':
        text.append(word[2:len(word)])
    elif not (word[0] == '#' and word[1] == '#' and word[2] == '#' and word[3] == '#'):
        text.append(word)
for i in range(len(text)):
    print(text[i])
