masa: 80
estatura: 1.56
def imc(masa, estatura):
  imc = 0
  # desde aquí hacia abajo debes modificar el programa
  imc = masa/(estatura**2)
  # modifica la variable imc
  # recuerda que los datos están en las variables masa y estatura
  return imc
IMC = imc(masa, estatura)
print(IMC)



distancia = 0.01 #kilometros
tiempo = 1 #segundos

def velocidad(distancia, tiempo):
  resultado = ""
  # desde aquí hacia abajo debes modificar el programa
  mdistancia = float(distancia)*1000
  htiempo = float(tiempo)/3600
  resultadoms = round(mdistancia/tiempo,2)
  resultadokh = round(distancia/htiempo,2)
  resultado = f"La velocidad es {resultadokh}k/h o {resultadoms}m/s"
  # modifica la variable resultado
  # recuerda que los datos están en las variables distancia y tiempo
  return resultado
print(velocidad(distancia,tiempo)) #imprimo la función llamandola 

a= True
b = True
def xor(a,b):
    xor = False
    if a==b:
      xor = False
    else:
       xor = True     
    return xor
print(xor(a,b))
