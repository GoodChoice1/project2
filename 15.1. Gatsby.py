print("Гэдсби")
letter=input()
text=input()
for i in range(len(text.split())):
    if letter in text.split()[i] or letter.upper() in text.split()[i]:
        print(text.split()[i])