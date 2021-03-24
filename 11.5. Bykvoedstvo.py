print("Буквоедство")
word = input()
first = 0
last = len(word)
while last - first > 0:
    print(word[first:last])
    first += 1
    last -= 1
