"""
productos = ["P001", "P002", "P003", "Cafe", "P005"]
producto_a_buscar = "Cafe"

for producto in productos:
  if producto == producto_a_buscar:
    print("Producto encontrado:", producto)
    break  
print("Fin de la búsqueda.")
"""

frutas = ["manzana", "banana", "naranja"]
for i in range(len(frutas)):
  print(f"Fruta {i+1}: {frutas[i]}")
