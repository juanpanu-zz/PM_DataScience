#Ejercicio#3: Diagrama de flujo
#Evaluando: Pensamiento Lógico
#Diseñe un programa mediante diagrama de flujo que defina si un número es primo o no.
#Recuerde que un número es primo si este es divisible solamente por 1 o por él mismo.
#Bonus: ¿Qué es un diagrama de flujo?
#El diagrama de flujo o también diagrama de actividades es una manera de representar
#gráficamente un algoritmo o un proceso de alguna naturaleza, a través de una serie de
#pasos estructurados y vinculados que permiten su revisión como un todo.

# Programa para definir si un numero es primo o no

#num = 3

# Entrada de usuario
num = int(input("ingrese un número: "))

# Números primos son mayores a 1.
if num > 1: 
   # Verificar Divisores
   for i in range(2,num):
       if (num % i) == 0: # Tiene un divisor entre 2 y él mismo - 1?
           print(num,"no es un número primo")
           print(i," veces",num//i,"es",num)
           break
   else:
       print(num,"es número primo")
       
# si la entrada es menor
# o igual a 1, no es primo
else:
   print(num,"no es número primo")