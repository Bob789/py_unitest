import math

def add(a: int(), b: int()):
    return a + b # + 0.1 # 0.99999999999

# 0.4444444444 + 0.66666666666
# 0.999999999999
# 1.0

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a: int, b: int):
    return a**b

def sqrt(a: int):
    if a < 0:
        raise ValueError("Sqrt parameter should be positive numbers.")
    return int(math.sqrt(a))

def factorial(a: int):
    resualt = 1
    if a > -1:
        while a > 1:
            resualt *= a
            a -=1
    else:
        raise ValueError("Factorial is not defined for negative numbers.")
    return resualt

def main():
    x = 3
    y = 7
    ap = 2
    bp = 4
    a = 9
    f = 5

    add(3,7)
    print(F"POWER {ap} ** {bp} = ",power(ap,bp))
    try:
        print(F"SQRT of {a} = ",sqrt(a))
    except ValueError as e:
        print(e)
    try:
        print(F"factorial of {f} = ",factorial(f))
    except ValueError as e:
        print(e)
if(__name__ == "__main__"):
    main()