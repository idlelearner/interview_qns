# Factorial of a number
def fact(n):
    return 1 if n == 0 else n * fact(n-1)

if __name__ == '__main__':
    print fact(5)
    print fact(0)
