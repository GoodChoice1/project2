print("Именно та буква")
word = input()
number = int(input())
lovedOne = input()
if number > len(word) or number < 1 or len(lovedOne) > 1:
    print("ОШИБКА")
elif word[number-1] == lovedOne:
    print("ДА")
