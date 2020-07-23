from autor import Autor
from contribucion import Contribucion

# def existCon(contribucion):
#     """Verificar si ya existe una contribución por ID de autor"""
#     MyCons=Contribucion.obInstances()
#     MyCons.pop()
#     temp=False
#     for instance in MyCons:
#         if contribucion == instance:
#             temp= True
#             break
#         else:  temp=False
#     return [temp, instance.idAutor]

# # def calificar(contribucion,puntaje):
# #     [existe,idAutor] =existCon(contribucion)
# #     if existe == False:
# #         contribucion.calificacion = puntaje
# #     else:
# #         pass


##Revisar Singleton
if __name__ == "__main__":
######## AUTORES ########
    autor = Autor()
    autor.id=123
    autor.nombre="Juan"
    autor.email = "juan.nunez@gmail.com"
    autor.universidad ="Harvard"
######## CONTRIBUCIONES ######
    contribucion = Contribucion()
    contribucion.id = 1
    contribucion.idAutor=autor.id
    contribucion.calificacion = 10
        
    contribucion2 = Contribucion()
    contribucion2.id = 2
    contribucion2.idAutor=autor.id
    contribucion2.calificacion = 10

    contribucion3 = Contribucion()
    contribucion2.id = 3
    contribucion3.idAutor=autor.id
    contribucion3.calificacion = 6
    # existe=existCon(contribucion3)
    # print(existe)
    contribucion4 = Contribucion()
    contribucion4.id = 4
    contribucion4.idAutor=autor.id
    contribucion4.calificacion = 8
###### Verificar calificacion ######
    myCont=Contribucion.obInstances()
    for instance in myCont:
        autor.verificarCalificacion(instance)

    publicaciones=autor.publicaciones
    listcal=autor.listcal
    calMax=autor.calificacionMax
    autor.calcularPromedio()
    promedio=autor.promedioCalificacion


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