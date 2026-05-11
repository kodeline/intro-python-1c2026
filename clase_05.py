# Contador Simple 
"""
contador = 0

while contador >= 0 and contador < 6:
  print(f"Este es el numero {contador}")
  contador += 1    
"""

# Solicitar el nombre mientras, no escriba nada 
"""
nombre = ""
contador = 1

while nombre == "":
  nombre = input("Ingrese su nombre: ")
  if nombre == "":
    print(f"Por favor ingrese su nombre por {contador} vez  ")
  contador += 1
  
print(f"Bienvenido/a {nombre}")
"""

# Validar contraseña con tres intentos
"""
intentos = 1 
max_intentos = 3
contrasenia ="python123"

while intentos <= max_intentos:
  clave = input("Ingrese su contraseña: ")
  if clave != contrasenia:
    print("contraseña incorrecta, intente de vuelta")
  else:
    print("Bienvenido")
  intentos += 1
print("Se ha bloqueado su usuario, por favor contacte al banco.")
"""


"""
intentos = 0
# Establecemos el máximo de intentos permitidos
max_intentos = 3
# Usamos un bucle que se detendrá si el usuario
# ingresa un nombre válido o si se agotan los intentos
while intentos < max_intentos:
   # Solicitamos al usuario que ingrese su nombre
   nombre = input("Ingresá tu nombre de usuario: ").strip()

# Verificamos si el nombre ingresado no está vacío
   if nombre != "":
       print(f"Bienvenido/a, {nombre}!")  # Mensaje de éxito
       break  # Salimos del bucle si se ingresa un nombre válido
   else:
       print("El nombre no puede estar vacío. Intentá de nuevo.")
   # Incrementamos el contador de intentos
   intentos += 1
# Verificamos si se agotaron los intentos
if intentos == max_intentos:
   print("Se agotaron los intentos. Intente más tarde.")
"""

"""
intentos = 0
max_intentos = 3
nombre = ""
while intentos < max_intentos and nombre == "":
  nombre = input("Ingresá tu nombre de usuario: ").strip()
  if nombre == "":
    print("El nombre no puede estar vacío. Intentá de nuevo.")
    intentos += 1

if nombre != "":
   print(f"Bienvenido/a, {nombre}!")
else:
   print("Se agotaron los intentos. Intente más tarde.")
"""

numero = 0
print("Ingresá números positivos para sumarlos. Ingresá 0 para terminar.")
suma = 0 
# primera vuelta suma = 2
# segunda vuelta suma = 4 
# tercera vuelta suma = 4
# cuarta vuelta suma = 6
# quinta vuelta suma = 6


while True:
   # Solicitamos al usuario un número
   numero = int(input("Ingresá un número: "))
   # Verificamos si el número es negativo
   if numero < 0:
      print("El número es negativo, se ignora. Intentá de nuevo.")
      continue  
   if numero == 0:
       break
   suma += numero
   
print(f"La suma de los números positivos es: {suma}")