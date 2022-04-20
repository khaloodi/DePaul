# Khaled Adad

def wordGame():
    import random

    text_file = open("Pride_and_Prejudice.txt", "r")
    strContents = text_file.read()
    text_file.close()

    p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for c in strContents:
        if c in p:
            strContents = strContents.replace(c, " ") 

    wordList = strContents.split()

    word_one = random.choice(wordList).lower()
    word_two = random.choice(wordList).lower()

    word_one_count = strContents.count(word_one)
    word_two_count = strContents.count(word_two)

    answer = input(f'Which word did the writer use more often "{word_one}" or "{word_two}"?')
    answer = answer.lower()

    if answer == word_one:
        if word_one_count > word_two_count:
            print('you are correct')
            print(f'Verification: "{word_one}" occurs {word_one_count} times, "{word_two}" occurs {word_two_count} times.')
        else:
            print('you are incorrect')
            print(f'Verification: "{word_one}" occurs {word_one_count} times, "{word_two}" occurs {word_two_count} times.')

    if answer == word_two:
        if word_two_count > word_one_count:
            print('you are correct')
            print(f'Verification: "{word_one}" occurs {word_one_count} times, "{word_two}" occurs {word_two_count} times.')
        else:
            print('you are incorrect')
            print(f'Verification: "{word_one}" occurs {word_one_count} times, "{word_two}" occurs {word_two_count} times.')


wordGame()