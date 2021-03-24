print("Ползём вниз")
map = input()
letter = map[0]
space = ' '
amountOfSpace = 0
text = letter
previousCommand = ''
amountOfRow = 0
for i in map[1:]:
    if i != previousCommand:
        amountOfRow = 0
    if i == '>':
        if previousCommand == 'V' or previousCommand == 'v':
            text = ''
            text += amountOfSpace * space + letter
        text += letter
        amountOfSpace += 1
        amountOfRow += 1
    elif i == '<':
        text += letter
        amountOfSpace -= 1
    elif (i == 'V' or i == 'v') and previousCommand == '<':
        text += amountOfSpace * space
        print(text[::-1])
        text = letter
    elif (i == 'V' or i == 'v') and previousCommand == '>':
        print(text)
        text = letter
    elif (i == 'V' or i == 'v') and previousCommand == 'V' or previousCommand == 'v' or previousCommand == '':
        print(amountOfSpace * space, letter, sep='')
    previousCommand = i
text += (amountOfSpace - amountOfRow) * space
if previousCommand == '>' or previousCommand == 'V' or previousCommand == 'v':
    print(text[::-1])
else:
    print(text)
