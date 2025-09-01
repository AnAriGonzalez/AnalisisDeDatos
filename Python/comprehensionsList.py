squares = [x**2 for x in range (1,11)]
#print("Cuadrados:", squares)

celsius =[0, 10, 20, 30, 40]
fahrenheit= [(temp* 9/5) +32 for temp in celsius]
print("temperatura F°:",fahrenheit)

#Numeros pares
even = [x for x in range (1, 21) if x%2 ==0]  #%2 "modulo dos" sirve para encontar números pares
print(even)

Matris = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in Matris] for i in range(len(Matris[0]))]
print(Matris)
print(transposed)


#lo mismo con más líneas de código:
transposed = []
for i in range(len(Matris[0])):
    transposed_row = []
    for row in Matris:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)