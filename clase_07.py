inventario = []
# productos = [ ["Queso","Lacteo","1500"] , ["Papas","Mercaderia",2500] ]


# Este es un producto solo 
producto = ["Queso","Lacteo","1500"]
inventario.append(producto)
print(f"Aca tengo el inventario con el producto: {inventario}")
mostrar_producto = inventario.pop()
print(f"En este punto se saco el ultimo elemento: {inventario}")
print(f"Aca se toma el elemento que sacamos de la lista: {mostrar_producto}")

# Usando el Sort 
letras = ["z","r","a","b","2","10"]
#letras.sort(reverse=True)
#print(f"letras ordenadas: {letras}")

# Cambiando lista a tupla 
tupla = tuple(letras)
print(letras)
print(tupla)

otra_lista = list(tupla)
print(otra_lista)

