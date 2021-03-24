print("Цезарь его знает")
number = int(input())
word = input()
answer = ""
for char in word:
    if (ord(char) + number) > 1103 and 1039 < ord(char) < 1104:
        char = chr(1040 + (ord(char) + number - 1103))
    elif (ord(char) + number) < 1040 and 1039 < ord(char) < 1104:
        char = chr(1103 - (1040 - (ord(char) + number)))
    elif 1039 < ord(char) < 1104:
        char = chr(ord(char)+number)
    answer += char
print(answer)