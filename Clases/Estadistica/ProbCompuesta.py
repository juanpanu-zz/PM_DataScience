from functools import reduce

def factorial(n):
  # Generar una lista de elementos desde 1 a n (Inicializado por defecto en 1, para factoriales 0)
  # Recorrer lista, y cada elemento multiplicarlo por el resultado anterior
  # Devolver resultado
  return reduce( lambda a, b: a * b, range(1, n+1), 1) 

def combinacion(n, r):
  return factorial(n) / (factorial(r) * factorial(n - r)) # Fórmula para calcular combinación

def variacion(n, r):
  return factorial(n) / factorial(n - r) # Fórmula para calcular variación

def permutacion(n):
  return factorial(n) # Fórmula para calcular permutación

if __name__ == '__main__':
  n = int(input('Ingresa el total de elementos "N": '))
  r = int(input('Ingresa el grupo "r": '))
  print('Variación: {}'.format( variacion(n, r)) )
  print('Combinación: {}'.format( combinacion(n, r)) )
  print('Permutación: {}'.format( permutacion(n)) )