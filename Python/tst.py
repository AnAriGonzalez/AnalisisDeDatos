
n = int(input("Introduce un número: "))

# Inicializar el resultado
res = 1

# Bucle para realizar la multiplicación
for i in range(1, n + 1):
    res *= i

# Imprimir el resultado
print(f"El resultado de la multiplicación de los números consecutivos de 1 a {n} es: {res}")