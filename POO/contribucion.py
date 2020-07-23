
class Contribucion:
    """Clase que representa la Contribucion"""
    instances = []
    def __init__(self, id = int, titulo = '*', idAutor = int, calificacion =int):
        self.__class__.instances.append(self)
        self.id = id
        self.titulo = titulo
        self.idAutor = idAutor
        self.calificacion = calificacion
        
    
    def actualizarAutor(self):
        pass

    @property    #ID Getter function 
    def id(self):
        return self._id

    @id.setter #ID Setter function
    def id(self,id):
        self._id = id

    @property    #titulo Getter function 
    def titulo(self):
        return self._titulo

    @titulo.setter #titulo Setter function
    def titulo(self,titulo):
        self._titulo = titulo

    @property    #idAutor Getter function 
    def idAutor(self):
        return self._idAutor

    @idAutor.setter #idAutor Setter function
    def idAutor(self,idAutor):
        self._idAutor = idAutor

    @property    #calificacion Getter function 
    def calificacion(self):
        return self._calificacion
      
    @calificacion.setter #calificacion Setter function
    def calificacion(self,calificacion):
        self._calificacion = calificacion
         
    def __eq__(self,contribucion):
        return self.idAutor == contribucion.idAutor

    @classmethod
    def obInstances(cls):
        return cls.instances
        
                
        
            
            
        