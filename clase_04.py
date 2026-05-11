# Dias de semana con elif 
"""
dia_semana = input("Que dia de la semana es hoy: ")

if dia_semana == 1:
  print("Lunes")
elif dia_semana == 2:
  print("Martes")
elif dia_semana == 3:
  print("Miercoles")
elif dia_semana == 4:
  print("Jueves")
elif dia_semana == 5:
  print("Viernes")
else:
  print("Esto no es un dia de la semana")
"""

# el semaforo
semaforo = input("Ingrese el color del semaforo: ")

# con match  
"""
match semaforo:
  case "verde":
    print("Avanzar")
  case "amarillo":
    print("Precaucion")
  case "rojo":
    print("Detenerse")
  case _:
    print("No es un color valido")
"""

# con elif 
if semaforo == "verde":
  print("Avanzar")
elif semaforo == "amarillo":
  print("Precaucion")
elif semaforo == "rojo":
  print("Detenerse")
else:
  print("Color no valido")