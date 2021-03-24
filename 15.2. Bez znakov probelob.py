print("Знаков без пробелов")
text=input()
letters=0
for i in range(len(text.split())):
    letters+=len(text.split()[i])
print(letters)