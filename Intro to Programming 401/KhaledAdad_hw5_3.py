# Khaled Adad
# HW 5 Problem 3

def upper_2():

    upperCaseFirstLetter = 0
    words = []
    word = (input('Enter a word: '))

    while len(word)>0:
        if word == '' or ' ' in word:
            break
        if word[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            upperCaseFirstLetter += 1
        words.append(word)
        word = (input('Enter a word: '))
    
    if len(words) == 0: 
        return '0 words were entered'

    return f'Words with upper case first letter = {upperCaseFirstLetter}'

print(upper_2())
    