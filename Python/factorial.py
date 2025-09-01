def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial_5 = print(factorial(80))


#fibonacci = función que genera numeros creados de la suma de los dos anteriores
def fibo(limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a, b = b, a+b
for num in fibo(10):
    print(num)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)