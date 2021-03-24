print("Розенкранц и Гильденстерн меняют профессию")
text = input()
maxRow = 0
thisRow = 0
for i in text:
    if i == 'о':
        thisRow += 1
        if thisRow > maxRow:
            maxRow = thisRow
    else:
        thisRow = 0
print(maxRow)
