print("Крупные буквы")
text = input()
first = ''
second = ''
third = ''
fourth = ''
fifth = ''
for i in text:
    if i == 'A':
        first += '  *   '
        second += ' * *  '
        third += '***** '
        fourth += '*   * '
        fifth += '*   * '
    elif i == 'B':
        first += '****  '
        second += '*   * '
        third += '****  '
        fourth += '*   * '
        fifth += '****  '
    elif i == 'C':
        first += ' **** '
        second += '*     '
        third += '*     '
        fourth += '*     '
        fifth += ' **** '
print(first)
print(second)
print(third)
print(fourth)
print(fifth)
