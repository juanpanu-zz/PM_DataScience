class Taller(Contribucion):
    """Clase que representa al Taller"""
    def __init__(self,id, titulo, idAutor,calificacion,capacidadMaxima = int,duracion= int):
        super().__init__(self, id, titulo, idAutor,calificacion)
        self.capacidadMaxima = capacidadMaxima
        self.duracion = duracion

    #capacidadMaxima Getter function 
    @property    
    def capacidadMaxima(self):
        return self._capacidadMaxima

    #capacidadMaxima Setter function
    @capacidadMaxima.setter
    def capacidadMaxima(self,capacidadMaxima):
        self._capacidadMaxima = capacidadMaxima

    #capacidadMaxima Getter function 
    @property    
    def capacidadMaxima(self):
        return self._capacidadMaxima

    #capacidadMaxima Setter function
    @capacidadMaxima.setter
    def capacidadMaxima(self,capacidadMaxima):
        self._capacidadMaxima = capacidadMaxima