print("bf")
commands = input()
lent = [0] * 30000
number = 0
i = 0
while i < len(commands):
    if commands[i] == '+':
        lent[number] += 1
        if lent[number] == 256:
            lent[number] = 0
    elif commands[i] == '.':
        print(lent[number])
    elif commands[i] == '>':
        number += 1
        if number == 30000:
            number = 0
    elif commands[i] == '<':
        number -= 1
        if number == -1:
            number = 29999
    elif commands[i] == '-':
        lent[number] -= 1
        if lent[number] == -1:
            lent[number] = 255
    elif commands[i] == '[':
        if lent[number] == 0:
            while commands[i] != ']':
                i += 1
        else:
            i += 1
            if commands[i] == '+':
                lent[number] = 255
            elif commands[i] == '-':
                lent[number] = 0
    i += 1
