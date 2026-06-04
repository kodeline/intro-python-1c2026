diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Buenos Aires"
}
"""
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

print("---------------------")
print(diccionario['ciudad'])
diccionario['ciudad'] = "Cordoba"
edad = diccionario.get('edad')

print(f"Soy {diccionario['nombre']} y vivo en {diccionario['ciudad']} y tengo {edad +10}")

if(diccionario.get('edad') - 10 >  18):
  print("Soy Mayor")
else:
  print("Soy Menor") 
"""
  
"""
print("------------METODOS DE DICCIONARIO--------------")
print(f"Estas son las claves {diccionario.keys()}")
print(f"Estas son los valores {diccionario.values()}")
print(f"Estas son los items {diccionario.items()}")
print(diccionario.popitem())
print(f"Estas son los items {diccionario.items()}")
"""

estudiantes = {
    "Ana": {"edad": 22, "carrera": "Informática"},
    "Juan": {"edad": 24, "carrera": "Diseño"}
}

print(estudiantes['Juan']['carrera'])
print(estudiantes.get('Juan').get('carrera'))

inventario = [
    {"nombre": "manzanas", "cantidad": 50},
    {"nombre": "peras", "cantidad": 30, 1 : "Hoola"},
    {"nombre": "naranjas", "cantidad": 40}
]

print(f"Stock: {inventario[2].get('cantidad')} - Nombre: {inventario[2].get('nombre')}")


