# Operadores relaciones 
"""
print(4>3)   # True 
print(2<1)   # False 
print(6==6)  # True
print(8!=8)  # False   

numero1 = "2"
numero2 = 4
"""

# Condicional IF
"""
if 2 > 4:
  print("Si es mayor")
else:
  print("No es mayor")
"""

"""
edad = 15
tiene_boleto = True

if edad >= 18 or tiene_boleto:   
  otra = 3
  otra2 = 45
  print("Podes pasar pibe/a")
else: 
  print("A casa pibe/a")
"""

# Clase Practica 
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
email = input("Ingrese su email: ")


if nombre and apellido and email and edad >= 18:
  print(nombre)
  print(apellido)
  print(edad)
  print(email) 
else:
  print("Error")


# Otra forma mas completa de resolver el ejercicio
"""
if nombre != "": 
  print("Nombre: " + nombre)
else:
  print("Error al ingresar nombre")

if apellido == "": 
  print("ERROR! al ingresar apellido")
else:
  print("Apellido: " + apellido)

if edad < 18: 
  print("ERROR! al ingresar edad")
else: 
  print("Edad:" + str(edad))

if email == "": 
  print("ERROR! al ingresar email")
else:
  print("email:" + email)
"""

