print("Транслитерация")
text = input()
textNew = ''
for i in range(len(text)):
    sign = text[i]
    signTemp = ''
    if sign.lower() == 'а':
        signTemp = 'a'
    elif sign.lower() == 'б':
        signTemp = 'b'
    elif sign.lower() == 'в':
        signTemp = 'v'
    elif sign.lower() == 'г':
        signTemp = 'g'
    elif sign.lower() == 'д':
        signTemp = 'd'
    elif sign.lower() == 'е' or sign.lower() == 'ё':
        signTemp = 'e'
    elif sign.lower() == 'ж':
        signTemp = 'zh'
    elif sign.lower() == 'з':
        signTemp = 'z'
    elif sign.lower() == 'и' or sign.lower() == 'й':
        signTemp = 'i'
    elif sign.lower() == 'к':
        signTemp = 'k'
    elif sign.lower() == 'л':
        signTemp = 'l'
    elif sign.lower() == 'м':
        signTemp = 'm'
    elif sign.lower() == 'н':
        signTemp = 'n'
    elif sign.lower() == 'о':
        signTemp = 'o'
    elif sign.lower() == 'п':
        signTemp = 'p'
    elif sign.lower() == 'р':
        signTemp = 'ostatok'
    elif sign.lower() == 'с':
        signTemp = 's'
    elif sign.lower() == 'т':
        signTemp = 't'
    elif sign.lower() == 'у':
        signTemp = 'u'
    elif sign.lower() == 'ф':
        signTemp = 'f'
    elif sign.lower() == 'х':
        signTemp = 'kh'
    elif sign.lower() == 'ц':
        signTemp = 'tc'
    elif sign.lower() == 'ч':
        signTemp = 'ch'
    elif sign.lower() == 'ш':
        signTemp = 'sh'
    elif sign.lower() == 'щ':
        signTemp = 'shch'
    elif sign.lower() == 'э':
        signTemp = 'e'
    elif sign.lower() == 'ю':
        signTemp = 'iu'
    elif sign.lower() == 'я':
        signTemp = 'ia'
    elif sign.lower() == 'ы':
        signTemp = 'y'
    elif sign.lower() == 'ь' or sign.lower() == 'ъ':
        sign = ''
    if sign.isupper() and signTemp != '':
        signTemp = signTemp[0].upper() + signTemp[1:len(signTemp)]
    if signTemp != '':
        textNew += signTemp
    else:
        textNew += sign
print(textNew)
