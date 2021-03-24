print("/etc/passwd")
text = ' '
logs = []
while text != '':
    text = input()
    if text == '':
        break
    else:
        logs.append(text)
passwords = input()
for i in range(len(logs)):
    for j in range(len(passwords.split(';'))):
        if logs[i].split(':')[1] == passwords.split(';')[j]:
            print('To:' + logs[i].split(':')[0])
            print(logs[i].split(':')[4].split(',')[0] + ", ваш пароль слишком простой, смените его.")