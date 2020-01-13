def factorial(n):
    if(n <= 1):
        return n
    return n * factorial(n-1)

def going(n):
    first = 1/factorial(n)
    second = sum([factorial(i) for i in range(n)])
    return 1 + first * second


print(going(8))
