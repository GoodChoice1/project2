print("RLE")
text = input() + " "
previous = ''
length = 1
for i in text:
    if previous == i:
        length += 1
    else:
        print(length, previous)
        length = 1
    previous = i
