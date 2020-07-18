class Taller(Contribucion):
    """Clase que representa al Taller"""
    def __init__(self,id, titulo, idAutor,calificacion,capacidadMaxima = int,duracion= int):
        super().__init__(self, id, titulo, idAutor,calificacion)
        self.capacidadMaxima = capacidadMaxima
        self.duracion = duracion
