import random

def moneda_aire(iteraciones):
    lanzamientos = 3
    lista = (0,1)

    lista_iteraciones = 0

    for _ in range(iteraciones):
        resultados = []
        
        for _ in range(lanzamientos):
            tiro = random.choice(lista)
            resultados.append(tiro)

        if sum(resultados) == 2:
            lista_iteraciones += 1

    return lista_iteraciones / iteraciones


def  factorial(numero):
    if numero <= 1:
        return 1

    else:
        return numero * factorial(numero - 1)

def  bolsa_pelotas():
    pelotas_totales = 3+6+3+9
    pelotas_roja_negra = 6+3
    return pelotas_roja_negra / pelotas_totales

def alcoholicos_higado():
    return 0.7 + 0.15 - 0.05

def variaciones(n,r):
    n_fact = factorial(n)
    return n_fact/factorial(n-r)

class Tablas_Frecuencias:
    def __init__(self, tupla):
        self.tupla = tupla 
        conjunto = set(self.tupla)
        lista_norepetida = list(conjunto)
        lista_norepetida.sort()
        self.n = len(tupla)                         #n (Numero de elementos en la lista)
        self.xi = lista_norepetida                  #X (Elementos en la lista sin repetir)
        self.ni = []                                #Frecuencia absoluta
        for i in self.xi:
            self.ni.append(tupla.count(i))
        self.Ni = []                                #Frecuencia absoluta acumulada
        for i in self.ni:
            acumulador = 0
            acumulador += i
            self.Ni.append(acumulador)
        self.fi = []                                #Frecuencia Relativa
        for i in self.ni:
            self.fi.append(i/self.n)
        self.Fi = []                                #Frecuencia Relativa Acumulada
        for i in self.Ni:
            self.Fi.append(i/self.n)

    def absoluta(self, index):
        indice = self.xi.index(index)
        return self.ni[indice]

    def relativa(self, index):
        indice = self.xi.index(index)
        return self.fi[indice]

    def clasificar_grupos(self, ls_grupos):
        temp_lista = list(self.tupla)
        temp_lista.sort()
        clasificacion = [0] * len(ls_grupos)
        while len(temp_lista) > 0:
            for i in range(len(ls_grupos)-1, 0-1, -1):
                try:
                    while temp_lista[-1] > ls_grupos[i-1] or i == 0:
                        if temp_lista[-1] <= ls_grupos[i]:
                            temp_lista.pop()
                            clasificacion[i] += 1
                except:
                    break                                                
        grafica = {}
        for i in range(len(ls_grupos)):
            grafica[ls_grupos[i]] = (clasificacion[i]/len(self.tupla))

        return grafica

    def media(self):
        return sum(self.tupla)/len(self.tupla)

    def mediana(self):
        temp_lista = list(self.tupla)
        temp_lista.sort()
        if len(temp_lista) % 2 == 0:
            print("Entro al par")
            print(temp_lista)
            indice1 = int(len(temp_lista)/2)-1
            indice2 = int((len(temp_lista)/2)+1)-1
            print(temp_lista[indice1])
            print(temp_lista[indice2])
            return (temp_lista[indice1] + temp_lista[indice2]) / 2
        else:
            indice = int((len(temp_lista)+1) / 2)-1
            return temp_lista[indice]

    def moda(self):
        indices = []
        modas = []
        numeracion = enumerate(self.ni)
        for lista in numeracion:
            if lista[1] == max(self.ni):
                indices.append(lista[0])
        for index in indices:
            modas.append(self.xi[index])

        return modas


    def varianza(self):
        lista_varianza = []
        mu = self.media()
        for i in self.tupla:
            lista_varianza.append((mu - i)**2)

        return sum(lista_varianza) / len(lista_varianza)

    def desviacion_estandar(self):
        varianza = self.varianza()
        return varianza**0.5


class Estadistica:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.media_x = sum(x)/len(x)
        self.media_y = sum(y)/ len(y)
        self.xi_yi = []
        for i in range(len(self.x)):
            self.xi_yi.append(self.x[i]*self.y[i])
        


    def media(self):
        return (self.media_x, self.media_y)



    def covarianza(self):
        return (sum(self.xi_yi)/len(self.xi_yi) - (self.media_x * self.media_y))

    def buscar_xi_yi(self, indice):
        index = self.x.index(indice)
        return self.xi_yi[index]









def seleccion(seleccion):

    if seleccion == 0:
        x = [5,11,10,8,9,8,6,1,4,3,3,3]
        y = [3,9,9,6,8,7,5,2,3,2,3,4]
        estadistica = Estadistica(x,y)
        return estadistica.covarianza()

    if seleccion == 1:
        iteraciones = int(input('''Ingrese cantidad de validaciones a realizar
(Se recomienda entre 1.000 y 10.000.000 para una mayor certeza el valor depende del rendimiento de tu equipo): '''))
        return moneda_aire(iteraciones)

    if seleccion == 2:
        numero = int(input('Ingrese un numero para Calcular su factorial: '))
        return factorial(numero)

    if seleccion == 3:
        return bolsa_pelotas()

    if seleccion == 4:
        return alcoholicos_higado()

    if seleccion == 5:
        n = int(input('Ingrese cuantos elementos tenemos:    '))
        r = int(input('Ingrese la cantidad de elementos por grupo:  '))
        return variaciones(n,r)

    if seleccion == 6:
        tupla = (98, 85, 94, 92, 100, 100, 86, 94, 100, 97, 96, 97, 100, 94, 84, 97, 100, 93, 100, 87)
        frecuencia = Tablas_Frecuencias(tupla)
        subpregunta = int(input('''
        
1. Frecuencia absoluta
2. Frecuencia relativa
3. Grafica de calificaciones
4. Media
5. Mediana
6. Moda
        
    Seleccione la subpregunta a responder:  '''))

        if subpregunta == 1:
            index = int(input('Ingrese el numero que desea calcular su frecuencia absoluta: '))
            return frecuencia.absoluta(index)

        if subpregunta == 2:
            index = int(input('Ingrese el numero que desea calcular su frecuencia absoluta: '))
            return frecuencia.relativa(index)

        if subpregunta == 3:
            ls_grupos = [85,90,95,100]
            return f"{frecuencia.clasificar_grupos(ls_grupos)} En caso de no entender que significa el dicionario la respuesta es la A"

        if subpregunta == 4:
            return frecuencia.media()

        if subpregunta == 5:
            return frecuencia.mediana()

        if subpregunta == 6:
            return frecuencia.moda()


    if seleccion == 7:
        tupla = (13, 7, 9, 15, 3, 10, 5, 10, 8, 2, 9, 9, 11, 7, 9, 7, 7, 7, 13, 11, 14, 9, 8, 13, 10, 16, 12, 12, 8, 6, 7, 8, 8, 13, 9, 7, 9, 8)
        frecuencia = Tablas_Frecuencias(tupla)
        estadistica = Estadistica(list(range(1,len(tupla)+1)), tupla)
        subpregunta = int(input('''
        
1. Media
2. Mediana
3. Moda
4. XiYi
5. Covarianza
        
    Seleccione la subpregunta a responder:  '''))

        if subpregunta == 1:
            return frecuencia.media()

        if subpregunta == 2:
            return frecuencia.mediana()

        if subpregunta == 3:
            return frecuencia.moda()

        if subpregunta == 4:
            indice = int(input('Ingrese el numero a buscar en X:   '))
            return estadistica.buscar_xi_yi(indice)
    
        if subpregunta == 5:
            return estadistica.covarianza()

    if seleccion == 8:
        tupla = (18,20,16,14)
        frecuencia = Tablas_Frecuencias(tupla)
        media = frecuencia.media()
        desviacion_estandar = frecuencia.desviacion_estandar()
        return (media + desviacion_estandar, media - desviacion_estandar)

    if seleccion == 9:
        return"Intersección de A y B"

    if seleccion == 10:
        return"Numerico"

    if seleccion == 11:
        return"Si P(A) < P(B), el evento A tiene una mayor probabilidad de ocurrir que en el evento B"

    if seleccion == 12:
        return"Espacio muestral"


if __name__ == '__main__':
    iniciar = 1
    while iniciar == 1:
        iniciar = int(input('''
¿Que desea realizar?
1. Consultar
0. Salir
'''))
        if iniciar == 1:
            pregunta = int(input('''
Seleccione la pregunta a consultar

1. Moneda al aire
2. factorial    
3. Bolsa de pelotas
4. Población Alcoholica + enfermedad de higado
5. variaciones
6. Calificacion de alumnos
7. Tabla de Goles
8. Zanahorrias (media +- Desviación estandar)
9. Es el suceso formado por todos los resultados que cumplen A y cumplen B:
10. Cuando lanzamos un dado esperando obtener cierto resultado, a partir de la cara que da hacia arriba, se trata de un experimento:
11. ¿Cuál de las siguientes afirmaciones es falsa?
12. Es el conjunto de elementos que representan a todos los posibles resultados de un experimento:


    Seleccione la pregunta a consultar: '''))

            resultado = seleccion(pregunta)

            print(f'Resultado = {resultado}')