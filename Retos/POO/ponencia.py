class Ponencia(Contribucion):
    """Clase que representa la Ponencia"""
    def __init__(self,id, titulo, idAutor,calificacion,fecha,eje):
        super().__init__(self, id, titulo, idAutor,calificacion)
        self.fechaPublicacion = fecha
        self.ejeTematico = eje

    #fechaPublicacion Getter function 
    @property    
    def fechaPublicacion(self):
        return self._fechaPublicacion

    #fechaPublicacion Setter function
    @fechaPublicacion.setter
    def fechaPublicacion(self,fechaPublicacion):
        self._fechaPublicacion = fechaPublicacion

    #ejeTematico Getter function 
    @property    
    def ejeTematico(self):
        return self._ejeTematico

    #ejeTematico Setter function
    @ejeTematico.setter
    def ejeTematico(self,ejeTematico):
        self._ejeTematico = ejeTematico
