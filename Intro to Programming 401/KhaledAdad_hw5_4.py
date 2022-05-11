# Khaled Adad
# HW 5 Problem 4

n = int(input('Enter row/column #: '))

def squareDiagonals(x):

    for i in range(x):
        for j in range(x):
            if (i == 0) or (i == (n-1)) or (j == 0) or (j ==(n-1)) or ((i+j) == (n-1)) or (j==i): #conditions for drawing a star we are on the border
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
squareDiagonals(n)