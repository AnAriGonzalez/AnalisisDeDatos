
"""Realizar las siguientes operaciones aritméticas e imprimir el resultado en pantalla:
a.- 265*3 + 88*4 - 960/5
"""
resultado = 265 * 3 + 88 * 4 - 960 / 5
print(resultado)

"""1a.- Resolver las siguientes expresiones lógicas:
a.- NOT (X AND Y OR X)                            
Si X= verdadero y Y= falso

"""

x = True
y = False
result = not(x and y or x)
print(result)

""" 1b.- NOT (A>B) OR (B>4) AND (A<=1)
      Si A = 5 y B = 8
"""

a = 5
b = 8
r = not(a>b) or (b>4) and (a<=1)
print(r)

"""2. - Construir una expresión lógica cuyo valor sea verdadero, si un número X se
encuentra en el intervalo [3,10), en caso contrario, debe ser falso.

"""

x = (int(input("Escribe un numero:")))
if x <10 and x >3:
  print(True)
else:
  print(False)

"""3.- Construir una expresión lógica cuyo valor sea verdadero, si la edad de una persona
es mayor a 60 años o menor a 12 años. El resultado de la expresión debe ser falso si X
se encuentra fuera de ese intervalo.

"""

edad = (int(input("Escribe tu edad:")))
if edad <=12 or edad >=60:
  print(True)
else:
  print(False)

"""4.- Construir una expresión lógica cuyo valor sea verdadero, si una persona es de sexo
femenino y tiene más de 25 años. En otros casos, el resultado de la expresión debe ser
falso.

"""

sexo = (str(input("escribe sexo f o m:")))
edad = (int(input("escribe tu edad:")))
if sexo =="f"and edad == 25:
  print(True)
else:
  print(False)

"""# 5. Escribe un programa en Python que:
• Solicite al usuario ingresar un número entero.
• Determine si el número ingresado es múltiplo de 3.
• Muestre un mensaje indicando si el número sí es múltiplo de 3 o no lo es.
Nota: Un número es múltiplo de 3 si al dividirlo por 3 el resto es cero.

"""

num = (int(input("escribe un numero entero:")))
resto = num%3
if resto == 0:
  print("Tu número es múltiplo de 3", True)
else:
  print(False)

"""# 6. Diseña un algoritmo en Python que calcule el salario neto de un trabajador en Chile.
El programa debe pedir al usuario:
• El salario base mensual en pesos chilenos (CLP)
• El número de hijos del trabajador
El cálculo del salario neto debe considerar lo siguiente:
- Se descuenta un 5% del salario base por concepto de seguro social.
- Si el trabajador tiene más de dos hijos, se le otorga un bono familiar adicional
de $50.000 CLP.
Finalmente, el programa debe mostrar en pantalla:
-El mo deontscontado por seguro social
-El bono por hijos (si corresponde)
-El salario neto final
Ejemplo de salida esperada:
Si el salario base es $600.000 CLP y el trabajador tiene 3 hijos:
Descuento por seguro social: $30.000
Bono por hijos: $50.000
Salario neto: $620.000

"""

salario_base = int(input("Ingrese el salario base mensual en CLP: ")) #int para transformar a n° entero el input
numero_hijos = int(input("Ingrese el número de hijos del trabajador: "))

descuento_SeguroSocial = salario_base * 0.05

bono_hijos = 0
if numero_hijos > 2:  #Deben ser más de 2 hijos para tener el beneficio
  bono_hijos = 50000

salario_neto = salario_base - descuento_SeguroSocial + bono_hijos

#Se agrega '$' antes del número de salida para que se lea como dinero
print(f"Descuento por seguro social: ${descuento_SeguroSocial:.0f}")
print(f"Bono por hijos: ${bono_hijos:.0f}")
print(f"Salario neto: ${salario_neto:.0f}")

"""8.- Diseñe un algoritmo que permita clasificar una especie forestal de acuerdo con su
resistencia. Tomando como dato de entrada el porcentaje de pérdida de peso de la
especie y la salida es uno de los siguientes mensajes:
Mensaje
Altamente Resistente
% Pérdida de Peso
Resistente
[0-1]
Moderadamente Resistente
(1-5]
Muy Poco Resistente
(5-10]
No Resistente
(10 – 30]
Más de 30

"""

#Este ejercicio consiste en la utilización de if, elif y else para clasificar el valor entregado en el input
Resist = (int(input("escribe el % de perdida de peso de la especie:")))
if Resist == 0 or Resist == 1:
  print("Altamente Resistente")
elif Resist >1 and Resist <=5:
  print("Moderadamente Resistente")
elif Resist >=6 and Resist <10:
  print("Muy poco Resistente")
elif Resist >=10 and Resist <=30:
  print("No Resistente")
elif Resist < 0:
    print ("Error: El porcentaje no puede ser negativo")
else:
  print("Ingresa un número entero")