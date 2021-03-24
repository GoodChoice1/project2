print("Какая то буква")
word = input()
numberOfChar = int(input()) - 1
if numberOfChar < 0 or numberOfChar > len(word):
    print("ОШИБКА")
else:
    print(word[numberOfChar])