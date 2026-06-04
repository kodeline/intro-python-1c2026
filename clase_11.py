from datetime import datetime
import random
import math
import clase_10
"""
def lanzar_dados():
  random1 = random.random()
  random2 = random.random()
  suma = random1 + random2
  print("Suma de dos numeros random entre 0 & 1: ", suma)

lanzar_dados()

radio = int(input("Ingrese el radio del circulo: "))
area = math.pi * math.pow(radio, 2)
print(f"El area de un circulo con radio {radio} es: {area}")
"""


fecha_hora_actual = datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)
print("Solo la fecha:", fecha_hora_actual.strftime("%d-%m-%Y"))
print("Solo la hora:", fecha_hora_actual.strftime("%H:%M:%S"))

# Esto sale de la funcion sumatoria que esta en clase_10.py
print(clase_10.sumatoria(5,4))
