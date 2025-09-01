a = [1,2,3,4,5,6]
b = a
print (a)
print (b)
del a [0] #sólo borró el primer elemento de la lista
print(id(a))
print(id(b)) #aquí podemos notar que a y b al ser copias una de otra utilizan el mismo lugar en memoria
print(a) #por lo tanto al cambiar a, b también sufrirá la modificación
print(b)
del b [3]

print(a)
print(b) # pasa lo mismo si borramos desde b