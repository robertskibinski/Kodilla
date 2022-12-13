def palindrom(s):
    return s == s[::-1]
word = input('Podaj słowo: ')
ret = palindrom(word)
if ret:
    print(f'{word} jest palindromem')
else:
    print(f'{word} nie jest palindromem')
