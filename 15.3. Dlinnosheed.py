print("Длинношеееед")
text = input()
max = 0
temp = 0
for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i].upper() == text[j].upper():
            if temp == 0:
                temp += 2
            else:
                temp += 1
    if temp > max:
        max, temp = temp, max
    temp = 0
print(max)
