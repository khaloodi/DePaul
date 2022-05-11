# Khaled Adad
# HW 5 Problem 1

example = [[1,3], [2,4],[0,8]]
example2 = [[1,2,3], [3,4,7], [0,5,2]]
example3 = [[1,3,4], [2,4]]
example4 = [[1,2,3,4], [8,9], [-6,6,7], [8,0,1,1]]

def evenRow(lst):
    def sumNums(lst):
        sum = 0
        for i in range(0,len(lst)):
            sum += lst[i]
        return sum

    for sub in lst:
        sum = sumNums(sub)
        # print(f'Returned sum value from sumNums: {sum}')
        if sum%2 == 0:
            continue
        else: 
            return False
    return True

print(evenRow(example))
print(evenRow(example2))
print(evenRow(example3))
print(evenRow(example4))