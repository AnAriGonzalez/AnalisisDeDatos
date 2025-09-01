x = 10
y = 15
# Al usar if, elif y else, else es el único que no requiere especificaciones.
if x>5:
    print(f"el valor {x} es mayor a 5")
elif x==5:
    print("El valor es 5")
else:
    print(f"{x} es menor a 5")

#And == ambas condiciones se deben cumplir
if x>=10 and y<20:
    print("Estrellita dónde estás")
else:
    print("Patatas fritas")
#Sólo una condición se debe cumplir
if x<5 or y==15:
    print("¡Eso no es justo!")
else:
    print("Dame esos 5")

fruits = ["Manzana","Pera","Uva","Piña","Naranja","Banana","Fresa"]
for fruta in fruits:
    print(fruta)
    if fruta =="Naranja":
        print("¡Naranja encontrada!") 
        break       
x = 0
while x<10:
    if x ==4:
        break
    print(x)
    x +=1
print("esto fue un break")
#continue
n = [1, 2, 3, 4, 5, 6]
for i in n:
    if i ==2:
        continue
    print("i es igual a:",i)

print("fin")