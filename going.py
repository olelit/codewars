from decimal import *

def factorial(n):
    if(n <= 1):
        return n
    return n * factorial(n-1)

def going(n):
    first = Decimal(1/factorial(n))
    print(first)
    second = Decimal(sum([factorial(i) for i in range(n)]))
    return first * second


print(going(200))
