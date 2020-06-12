# Ejercicio #2: Ordenamiento en listas.
# Tecnologías sugeridas: Python o Javascript (elegir), Git
# Realizar un programa que dada un lista de números desordenada, retorne una lista con
# todos sus valores ordenados de menor a mayor. No se puede utilizar la función “sort” u
# otras existentes en Javascript para el ordenamiento de la lista. ordenar([5,2,4,1]) = [1,2,4,5]
import random
print("Lista Desordenada")
unordered = list(range(10))
random.shuffle(unordered)
print(unordered)

def ordenar(lista): 
	n= len(lista)
	for i in range(n): 				#Se recorre toda la lista
		intercambio= False 			#inicializo variable para identificar si existe intercambio
							#Se asume que el último elemento queda organizado
		for j in range(0, n-i-1): 	 
							#Se recorre la lista desde 0 hasta n-i-1. 
							#Se intercambia si el elemento encontrado es mayor que el siguiente
			if lista[j] > lista[j+1]: #
				lista[j],lista[j+1] = lista[j+1], lista[j]
				intercambio=True
		if intercambio == False:
			break
	return(lista)

listaOrdenada=ordenar(unordered) # llamo a mi funcion y 

print("Lista Ordenada ")
print(listaOrdenada)

	