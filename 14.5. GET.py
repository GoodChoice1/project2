print("GET")
text = input()
key = input()
key = text.find(key) + len(key) + 1
answer=''
while text[key]!='?' and text[key]!='&' and text[key]!='=' and text[key]!='#' and key!=len(text)-1:
    answer+=text[key]
    key += 1
    if key==len(text)-1:
        answer+=text[key]
print(answer)
