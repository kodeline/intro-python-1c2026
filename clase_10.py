
def sumatoria(num1,num2):
  return num1 + num2


def calculadora(num1, num2):
  """
  La variable suma esta sumando, lo que yo escriba aca seria la documentacion 
  """
  suma = num1 + num2
  resta = num1 - num2
  multip = num1 * num2
  divis = num1 / num2
  return suma, resta, multip, divis

suma, resta, multip, divis = calculadora(4,2)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multip)
print("Division:", int(divis))

multiplicacion = suma * resta
print("Otra Multiplicacion:", multiplicacion )



