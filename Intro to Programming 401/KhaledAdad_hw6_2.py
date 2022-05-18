# Khaled Adad
# HW 6 Problem 2
import string

def wordSearch(fname, wordLst):
    f = open(fname, 'r')
    print(f)
    lines = len(f.readlines())
    print(lines)
    accumulator = 0

    index = {}
    for word in wordLst:
        index[word] = []
    print(f'Initial index: {index}')
    p = string.punctuation.replace("'", " ")
    print(f'P is: {p}')

    line = f.readline()
    print(f'My first line: {line}')
    while line:
        print(f'My second line: {line}')
        accumulator += 1
        words = line.split()
        for char in p:
            if char in words:
                print(true)
                words.remove(char)

        new_line = ' '.join(words)

        for word in wordLst:
            if word in new_line:
                index[word].append(accumulator)       
        print(new_line)          
        line = f.readline()
    f.close()
    return index

print(wordSearch('Pride_and_Prejudice.txt', ["Kent"]))