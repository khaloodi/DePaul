def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    
def choose(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

# illinois lottery
print(choose(52,6))

print(choose(100,20))

print(choose(100,50))