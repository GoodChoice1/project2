def sort(array):
    for j in range(len(array)):
        for i in range(len(array) - 1):
            if ord(array[i].split('/')[0][0]) > ord(array[i + 1].split('/')[0][0]):
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


def tell(array):
    for i in range(len(array)):
        print(array[i].split('/')[0])


print("Финал и не финал")
amount = int(input())
result = []
resultFirst = []
for i in range(amount):
    name = input()
    score = input()
    result.append(name + "/" + score)
for j in range(len(result)):
    for i in range(len(result) - 1):
        if int(result[i].split('/')[1]) > int(result[i + 1].split('/')[1]):
            result[i], result[i + 1] = result[i + 1], result[i]
temp = len(result) - 1
for i in range(len(result) // 2):
    resultFirst.append(result[temp])
    result.pop()
    temp -= 1
result = sort(result)
resultFirst = sort(resultFirst)
tell(resultFirst)
tell(result)
