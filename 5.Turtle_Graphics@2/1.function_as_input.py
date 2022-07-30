# Passing function as an input to the other function.

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculate(n1, n2, func):  # This function also called as "Higher-Order Function".
    return func(n1, n2)       # Since, it holds the other function in it.

result1 = calculate(2, 3, add)
print(result1)

result2 = calculate(2, 3, sub)
print(result2)

result3 = calculate(2, 3, mul)
print(result3)

result4 = calculate(2, 3, div)
print(result4)