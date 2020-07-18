#import datetime??

class Ponencia(Contribucion):
    """Clase que representa la Ponencia"""
    def __init__(self,id, titulo, idAutor,calificacion,fecha,eje):
        super().__init__(self, id, titulo, idAutor,calificacion)
        self.fechaPublicacion = fecha
        self.ejeTematico = eje


