# Ejemplo de la calculadora 
def calculadora(a, b):
  suma = a + b
  resta = a - b
  multi = a * b
  divis = a / b
  return suma, resta, multi, divis

suma, resta, multi, divis = calculadora(100,1)

def calcular_iva_producto():
  iva = suma * 1.21 

precio_iva = calcular_iva_producto()

def valor_total_productos(stock):
  total = precio_iva * stock  
  return total

print("El valor total de productos con IVA: ", valor_total_productos(10))