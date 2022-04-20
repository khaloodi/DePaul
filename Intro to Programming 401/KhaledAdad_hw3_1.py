# Khaled Adad

def formats(num):
    if num not in range(1,101):
        print('num should be in the range of 1 to 100')
        return 
    import random
    lst = []
    #lst is a list that contains 100 float numbers
    for i in range(100):
        lst.append(random.uniform(0,1000))
    
    str3 = '${: 6.2f}     ${: 6.2f}     ${: 6.2f}'
    str2 = '${: 6.2f}     ${: 6.2f}'
    str1 = '${: 6.2f}'

    if (num%3 == 0):
        for i in range (0, num, 3):
            print(str3.format(lst[i], lst[i+1], lst[i+2]))
    if (num%3 == 2):
        for i in range (0, num-3, 3):
            print(str3.format(lst[i], lst[i+1], lst[i+2]))
        print(str2.format(lst[i], lst[i+1]))
    if (num%3 == 1):
        # for i in range (0, num):
        #     print(str1.format(lst[i]))
        for i in range (0, num-3, 3):
            print(str3.format(lst[i], lst[i+1], lst[i+2]))
        print(str1.format(lst[i]))

print(formats(9))