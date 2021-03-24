print("Масштабирование")
height = int(input())
width = int(input())
image = []
for i in range(height):
    image.append(input())
imageSmall = []
text = ''
for i in range(height):
    if i % 2 == 0:
        for j in range(width):
            if j % 2 == 0:
                text += image[i][j]
        imageSmall.append(text)
        text=''
for i in range(len(imageSmall)):
    print(imageSmall[i])
