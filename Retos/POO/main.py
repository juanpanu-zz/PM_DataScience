from autor import Autor
from contribucion import Contribucion

def verificacion(autor):
    """
        Se utiliza el metodo de la clase Contribucion para
        obtener la cantidad de objetos instanciados.

        Se inicialista una lista de calificaciones como lista vacia

        por cada contribucion se realiza el llamado al metodo del autor
        para verificar calificacion que recibe como parametro la contribucion instanciada
        internamente en el metodo de verificacion del autor se actualizan las variables y 
        se retornan para ser usadas posteriormente
    """
    myCont=Contribucion.obInstances()
    autor.listcal=[]
    for instance in myCont:
        autor.verificarCalificacion(instance)

    publicaciones=autor.publicaciones
    listcal=autor.listcal
    calMax=autor.calificacionMax
    autor.calcularPromedio()
    promedio=autor.promedioCalificacion
    return [publicaciones,listcal,calMax,promedio]

##Revisar Singleton
if __name__ == "__main__":
############ AUTORES ############
    autor = Autor()
    autor.id=123
    autor.nombre="Juan"
    autor.email = "juan.nunez@gmail.com"
    autor.universidad ="Harvard"
############ CONTRIBUCIONES ############
    contribucion = Contribucion()
    contribucion.id = 1
    contribucion.idAutor=autor.id
    contribucion.calificacion = 10
        
    contribucion2 = Contribucion()
    contribucion2.id = 2
    contribucion2.idAutor=1
    contribucion2.calificacion = 10

    contribucion3 = Contribucion()
    contribucion3.id = 3
    contribucion3.idAutor=2
    contribucion3.calificacion = 6

    contribucion4 = Contribucion()
    contribucion4.id = 4
    contribucion4.idAutor=3
    contribucion4.calificacion = 8

    contribucion5 = Contribucion()
    contribucion5.id = 5
    contribucion5.idAutor=165
    contribucion5.calificacion = 8
############ Verificar calificacion ############
    #Usa el metodo verificacion del inicio
    [publicaciones,listcal,calMax,promedio]= verificacion(autor)



    my_str = "Datos del Autor"
    my_print= f"""    El nombre del autor es: {autor.nombre}
    El id del autor es: {autor.id}
    El correo del autor es: {autor.email}
    La Universidad es {autor.universidad}
    La cantidad de publicaciones es {publicaciones}
    Lista  de calificaciones {listcal}
    Su calificación máxima es {calMax}
    Promedio calificaciones es {promedio}

    """
    print(my_str.center(50,"#"))
    print(my_print)   


############ AUTORES ############
    autor2 = Autor()
    autor2.id=147
    autor2.nombre="Juan"
    autor2.email = "juan.nunez@gmail.com"
    autor2.universidad ="Harvard"
############ CONTRIBUCIONES ############
    contribucion11 = Contribucion()
    contribucion.id = 1
    contribucion.idAutor=autor2.id
    contribucion.calificacion = 10
        
    contribucion12 = Contribucion()
    contribucion12.id = 2
    contribucion12.idAutor=autor2.id
    contribucion12.calificacion = 10

    contribucion13 = Contribucion()
    contribucion13.id = 3
    contribucion13.idAutor=autor2.id
    contribucion13.calificacion = 6

    contribucion14 = Contribucion()
    contribucion14.id = 4
    contribucion14.idAutor=autor2.id
    contribucion14.calificacion = 8

    contribucion15 = Contribucion()
    contribucion15.id = 5
    contribucion15.idAutor=autor2.id
    contribucion15.calificacion = 8
############ Verificar calificacion ############
    #Usa el metodo verificacion del inicio
    [publicaciones,listcal,calMax,promedio]= verificacion(autor2)


    my_str = "Datos del Autor"
    my_print= f"""    El nombre del autor2 es: {autor2.nombre}
    El id del autor2 es: {autor2.id}
    El correo del autor2 es: {autor2.email}
    La Universidad es {autor2.universidad}
    La cantidad de publicaciones es {publicaciones}
    Lista  de calificaciones {listcal}
    Su calificación máxima es {calMax}
    Promedio calificaciones es {promedio}

    """
    print(my_str.center(50,"#"))
    print(my_print)  