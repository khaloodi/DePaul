# Khaled Adad
# HW 5 Problem 2

def upper_1():

    words = []
    upperCaseFirstLetter = 0

    while True:
        prompt = (input('Enter a word: '))

        if prompt == '' or ' ' in prompt:
            break

        if prompt[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            upperCaseFirstLetter += 1
        words.append(prompt)
        print(words)

    if len(words) == 0:
        return '0 words were entered'

    return f'Words with upper case first letter = {upperCaseFirstLetter}'

print(upper_1())
    