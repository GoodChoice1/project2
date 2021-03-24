print("Пристраивааемся в очередь")
amount = int(input())
queue = []
for i in range(amount):
    text = input()
    smallText = text[len(text) - 2: len(text)]
    if smallText == "ь.":
        surname = text[0:len(text) - 17]
        if surname[len(surname) - 1] == ' ':
            queue.append(surname[0:len(surname) - 1])
        else:
            queue.append(surname)
    elif smallText == "й.":
        surname1 = ''
        surname2 = ''
        j = 8
        while text[j] != '!':
            surname1 += text[j]
            j += 1
        j += 2
        while text[j] != ' ':
            surname2 += text[j]
            j += 1
        for j in range(len(queue)):
            if queue[j] == surname1:
                queue.insert(j+1, surname2)
                break
    elif smallText == "а.":
        for j in range(len(queue)):
            if queue[j] == text[0:len(text) - 34]:
                queue.pop(j)
                break
for i in range(len(queue)):
    print(queue[i])
