productos = {}

while True:
    print("\n- Agregar Producto -")
    nombre = input("Ingresa el nombre del producto o 'fin' para finalizar: ").strip().capitalize()
    
    if nombre.lower() == 'fin':
        print("\nCarga finalizada.")
        break
    
    precio = float(input(f"Ingresa el precio de {nombre}: $ "))   
    productos.update({nombre:precio})
    print(f"Diccionario actual: {productos}")

print("Inventario: ")
print(productos)