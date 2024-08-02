def fib_recursive(n, a=0, b=1):
    if n <= 0:
        return
    elif n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        fib_recursive(n - 1, b, a + b)

# Example call with 5 terms
fib_recursive(5)
