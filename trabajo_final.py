usuario_admin = "admin"
contrasenia = "1234"
 
# --- Aca hacemos el login ---
print("-------------------------------------")
print("         ACCESO AL SISTEMA")
print("-------------------------------------")
 
intentos = 0
acceso = False
 
while intentos < 3:
  usuario_input = input("Usuario: ").strip()
  contrasena_input = input("Contraseña: ").strip()
 
  if usuario_input == usuario_admin and contrasena_input == contrasenia:
    acceso = True
    print("Bienvenido/a al sistema.")
    break
  else:
    intentos += 1
    intentos_restantes = 3 - intentos
    
    if intentos_restantes > 0:
      print(f"Usuario o contraseña incorrectos. Te quedan {intentos_restantes} intento(s).\n")
    else:
      print("No tenes acceso. Superaste el límite de intentos.")
 
# Llegamos aca solo si el usuario se pudo logear 
# La parte de arriba osea el login no va para la pre-entrega
# A PARTIR DE ACA ABAJO ES LO QUE SE PIDE EN LA PRE-ENTREGA

if acceso:
    productos = []  # Aca cada producto es una sublista: producto = [nombre, categoria, precio]
 
    salir = False
 
    while not salir:
 
        print("--------------------------------------")
        print("  SISTEMA DE GESTION DE PRODUCTOS")
        print("--------------------------------------")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print("--------------------------------------")
 
        opcion = input("Elegí una opción (1-5): ").strip()
 
        match opcion:
 
            case "1":
                print("----- AGREGAR PRODUCTO -----")
 
                nombre = ""
                while nombre == "":
                    nombre = input("Nombre del producto: ").strip()
                    if nombre == "":
                        print("Error: el nombre no puede estar vacío.")
 
                categoria = ""
                while categoria == "":
                    categoria = input("Categoría del producto: ").strip()
                    if categoria == "":
                        print("Error: la categoría no puede estar vacía.")
 
                precio_valido = False
                while not precio_valido:
                    precio_input = input("Precio (sin centavos): ").strip()
                    if precio_input == "":
                        print("Error: el precio no puede estar vacío.")
                    elif not precio_input.isdigit():
                        print("Error: el precio debe ser un número entero positivo.")
                    elif int(precio_input) <= 0:
                        print("Error: el precio debe ser mayor a cero.")
                    else:
                        precio = int(precio_input)
                        precio_valido = True
 
                producto = [nombre, categoria, precio]
                productos.append(producto)
                print(f"Producto '{nombre}' agregado correctamente.")
            # Mostrar Producto
            case "2":
                print("----- PRODUCTOS REGISTRADOS -----")
 
                if len(productos) == 0:
                    print("No hay productos registrados.")
                else:
                    for i in range(len(productos)):
                        print(f"\n  N° {i + 1}")
                        print(f"  Nombre    : {productos[i][0]}")
                        print(f"  Categoría : {productos[i][1]}")
                        print(f"  Precio    : ${productos[i][2]}")
                    print(f"\nTotal de productos: {len(productos)}")
            # Buscar Producto
            case "3":
                print("---- BUSCAR PRODUCTO ----")
 
                if len(productos) == 0:
                    print("No hay productos registrados para buscar.")
                else:
                    busqueda = ""
                    while busqueda == "":
                        busqueda = input("Ingresá el nombre a buscar: ").strip()
                        if busqueda == "":
                            print("Error: el nombre no puede estar vacío.")
                 
                    encontrados = 0
                    for i in range(len(productos)):
                        if busqueda.lower() in productos[i][0].lower():
                            print(f"\n  N° {i + 1}")
                            print(f"  Nombre    : {productos[i][0]}")
                            print(f"  Categoría : {productos[i][1]}")
                            print(f"  Precio    : ${productos[i][2]}")
                            encontrados += 1
 
                    if encontrados == 0:
                        print(f"No se encontraron productos con el nombre '{busqueda}'.")
            # Eliminar Producto
            case "4":
                print("---- ELIMINAR PRODUCTO ----")
 
                if len(productos) == 0:
                    print("No hay productos registrados para eliminar.")
                else:
                    for i in range(len(productos)):
                        print(f"\n  N° {i + 1}")
                        print(f"  Nombre    : {productos[i][0]}")
                        print(f"  Categoría : {productos[i][1]}")
                        print(f"  Precio    : ${productos[i][2]}")
 
                    numero_valido = False
                    while not numero_valido:
                        numero_input = input("Ingrese el numero del producto a eliminar: ").strip()
                        if numero_input == "":
                            print("Error: el número no puede estar vacio.")
                        elif not numero_input.isdigit():
                            print("Error: ingrese un número válido.")
                        elif int(numero_input) < 1 or int(numero_input) > len(productos):
                            print(f"Error: ingrese un número entre 1 y {len(productos)}.")
                        else:
                            numero_valido = True
 
                    numero = int(numero_input)
                    nombre_eliminado = productos[numero - 1][0]
                    productos.pop(numero - 1)
                    print(f"\nProducto '{nombre_eliminado}' eliminado correctamente.")
 
            case "5":
                print("Ha cerrado la sesion del sistema...")
                salir = True
 
            case _:
                print("Opcion invalida. Elige una opción entre 1 y 5.")