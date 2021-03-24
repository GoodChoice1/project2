print("Телефонная книга")
length=int(input())
book=[]
answers=[]
for i in range(length):
    book.append(input())
length=int(input())
for i in range(length):
    name = input()
    answer=''
    for j in range(len(book)):
        if book[j].split()[1] == name:
            answer+=book[j].split()[0] + " "
    if answer!='':
        answers.append(answer)
    else:
        answers.append("Нет в телефонной книге")
for i in range(len(answers)):
    print(answers[i])