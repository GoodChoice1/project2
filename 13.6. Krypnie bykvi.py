print("Крупные буквы - 2")
text = input()
first = ''
second = ''
third = ''
fourth = ''
fifth = ''
for i in text:
    if i == 'A':
        first += ' *   '
        second += '* *  '
        third += '***  '
        fourth += '* *  '
        fifth += '* *  '
    elif i == 'B':
        first += '**   '
        second += '* *  '
        third += '**   '
        fourth += '* *  '
        fifth += '**   '
    elif i == 'C':
        first += ' *   '
        second += '* *  '
        third += '*    '
        fourth += '* *  '
        fifth += ' *   '
    elif i == 'D':
        first += '**   '
        second += '* *  '
        third += '* *  '
        fourth += '* *  '
        fifth += '**   '
    elif i == 'E':
        first += '***  '
        second += '*    '
        third += '**   '
        fourth += '*    '
        fifth += '***  '
    elif i == 'F':
        first += '***  '
        second += '*    '
        third += '**   '
        fourth += '*    '
        fifth += '*    '
    elif i == 'G':
        first += ' **  '
        second += '*    '
        third += '* *  '
        fourth += '* *  '
        fifth += ' **  '
    elif i == 'H':
        first += '* *  '
        second += '* *  '
        third += '***  '
        fourth += '* *  '
        fifth += '* *  '
    elif i == 'I':
        first += '***  '
        second += ' *   '
        third += ' *   '
        fourth += ' *   '
        fifth += '***  '
    elif i == 'J':
        first += ' **  '
        second += '  *  '
        third += '  *  '
        fourth += '* *  '
        fifth += ' *   '
    elif i == 'K':
        first += '* *  '
        second += '**   '
        third += '*    '
        fourth += '**   '
        fifth += '* *  '
    elif i == 'L':
        first += '*    '
        second += '*    '
        third += '*    '
        fourth += '*    '
        fifth += '***  '
    elif i == 'M':
        first += '* *  '
        second += '***  '
        third += '***  '
        fourth += '***  '
        fifth += '* *  '
    elif i == 'N':
        first += '* *  '
        second += '***  '
        third += '***  '
        fourth += '* *  '
        fifth += '* *  '
    elif i == 'O':
        first += '***  '
        second += '* *  '
        third += '* *  '
        fourth += '* *  '
        fifth += '***  '
    elif i == 'P':
        first += '***  '
        second += '* *  '
        third += '***  '
        fourth += '*    '
        fifth += '*    '
    elif i == 'Q':
        first += '***  '
        second += '* *  '
        third += '* *  '
        fourth += '***  '
        fifth += '  *  '
    elif i == 'R':
        first += '***  '
        second += '* *  '
        third += '***  '
        fourth += '**   '
        fifth += '* *  '
    elif i == 'S':
        first += '***  '
        second += '*    '
        third += '***  '
        fourth += '  *  '
        fifth += '***  '
    elif i == 'T':
        first += '***  '
        second += ' *   '
        third += ' *   '
        fourth += ' *   '
        fifth += ' *   '
    elif i == 'U':
        first += '* *  '
        second += '* *  '
        third += '* *  '
        fourth += '* *  '
        fifth += '***  '
    elif i == 'V':
        first += '* *  '
        second += '* *  '
        third += '* *  '
        fourth += '***  '
        fifth += ' *   '
    elif i == 'W':
        first += '***  '
        second += '***  '
        third += '***  '
        fourth += '***  '
        fifth += '***  '
    elif i == 'X':
        first += '* *  '
        second += '* *  '
        third += ' *   '
        fourth += '* *  '
        fifth += '* *  '
    elif i == 'Y':
        first += '* *  '
        second += '* *  '
        third += ' *   '
        fourth += ' *   '
        fifth += ' *   '
    elif i == 'Z':
        first += '***  '
        second += '  *  '
        third += ' *   '
        fourth += '*    '
        fifth += '***  '
print(first)
print(second)
print(third)
print(fourth)
print(fifth)