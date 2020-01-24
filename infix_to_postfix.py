def to_postfix(infix):

    excl = ['+','-', '*', '/']

    numbers = []
    symbols = []
    infix = infix.replace('(','')
    infix = infix.replace(')','')

    for item in infix:
        if item in excl:
            symbols.append(item)
        else: numbers.append(item)

    print(symbols)
    print(numbers)

    pass


print(to_postfix("2+7*5"))
print(to_postfix("(5-4-1)+9/5/2-7/1/7"))
