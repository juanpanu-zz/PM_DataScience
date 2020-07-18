from autor import Autor
## Revisar Singleton
if __name__ == "__main__":
    autor = Autor()
    autor.id="123"
    autor.nombre="Juan"
    autor.email = "juan.nunez@gmail.com"

    nombre2=autor.nombre
    print(nombre2)









    my_str = "Datos del Autor"
    my_print= f"""    El nombre del autor es: {autor.nombre}
    El id del autor es: {autor.id}
    El correo del autor es: {autor.email}
    nuevalinea
    """
    print(my_str.center(50,"#"))
    print(my_print)   