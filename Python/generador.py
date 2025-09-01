def migenerador():
    yield 1
    yield 2
    yield 3
for value in migenerador():
    print(value)

print("generador de números en sumatoria")

    #fibonacci = función que genera numeros creados de la suma de los dos anteriores
def fibo(limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a, b = b, a+b
for num in fibo(10):
    print(num)


