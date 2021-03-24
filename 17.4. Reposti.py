def addViews(arr, number, views):
    originalName = arr[number][2]
    while arr[number][0] != originalName:
        number -= 1
    arr[number][1] += views
    if arr[number][2] != '':
        arr = addViews(arr, number, views)
    return arr


print("Репосты")
length = int(input())
info = [[''] * 3 for i in range(length)]
for i in range(length):
    text = input()
    info[i][0] = text.split()[0]
    info[i][1] = int(text.split()[-1])
    if text.split()[3] == 'у':
        info[i][2] = text.split()[4][:-1]
        info = addViews(info, i, info[i][1])
for i in range(length):
    print(info[i][1])
