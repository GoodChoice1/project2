print("Бактериям бой!")
n = int(input())
field = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        field[i][j] = int(input())
amount = int(input())
for i in range(amount):
    y = int(input())
    x = int(input())
    field[x][y] -= 8
    if x - 1 >= 0:
        if y - 1 >= 0:
            field[x - 1][y - 1] -= 4
        field[x - 1][y] -= 4
        if y + 1 <= n - 1:
            field[x - 1][y + 1] -= 4
    if x + 1 <= n - 1:
        if y - 1 >= 0:
            field[x + 1][y - 1] -= 4
        field[x + 1][y] -= 4
        if y + 1 <= n - 1:
            field[x + 1][y + 1] -= 4
    if y - 1 >= 0:
        field[x][y - 1] -= 4
    if y + 1 <= n - 1:
        field[x][y + 1] -= 4
for i in range(n):
    for j in range(n):
        if field[i][j] < 0:
            field[i][j] = 0
        print(field[i][j], end=" ")
    print("")
