print("Посещаемость")
pages = int(input())
students = []
wasInClass = []
amount = int(input())
for i in range(amount):
    students.append(input())
    wasInClass.append(int(0))
for i in range(pages - 1):
    amount = int(input())
    for j in range(amount):
        surname = input()
        for k in range(len(students)):
            if students[k] == surname:
                wasInClass[k] += 1
for i in range(len(students)):
    if wasInClass[i] == (pages-1):
        print(students[i])