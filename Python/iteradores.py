#Este es un iterador
#primero se crea una lista
lista = [1, 2, 3, 4, 5]

#luego creamos un iterador
my_iter = iter(lista)

#usar el iterador
print(next(my_iter)) # este comando recorre la lista para imprimir uno a uno los enunciados. Podría terminar el código aquí, pero.... decidí que imprima todo
for float in my_iter: #si añado un loop for, puedo imprimir cada elemento en la lista de iteración
    print(float)
#Iterar en cadenas == aparecer cada caracter, uno a uno.

print("Iteración en texto")

hola = "Hello Kitty"
iter_text = iter(hola)
#Iterar en la cadena (string)
for char in iter_text:
    print(char)


#Iterador de números impares
print("iteración de números impares:")
limit = 10 #Establesco mi n° límite
imp_itter = iter(range(1,limit+1,2)) #creo mi iterador rango:(n° inicio, n° final, saltos )
#para imprimir mi iterador:
for num in imp_itter:
    print(num)

#Iterador de números impares
print("iteración de números pares:")
limit = 10 #Establesco mi n° límite
par_itter = iter(range(2,limit+1,2)) #creo mi iterador rango:(n° inicio, n° final, saltos )
#para imprimir mi iterador:
for num in par_itter:
    print(num)
