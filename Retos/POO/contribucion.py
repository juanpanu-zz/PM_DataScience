
class Contribucion:
    """Clase que representa la Contribucion"""
    instances = []
    def __init__(self, id = int, titulo = '*', idAutor = int, calificacion =int):
        self.__class__.instances.append(self)
        self.id = id
        self.titulo = titulo
        self.idAutor = idAutor
        self.calificacion = calificacion
        
    
    def actualizarAutor(self,nuevoid):
        """
            Actualiza el id del autor en una contribución
            #Nota:  cada vez que se actualice debe ejecutarse
                    el metodo de verificar autor desde el main.
        """
        self._idAutor=nuevoid

    #ID Getter function 
    @property    
    def id(self):
        return self._id

    #ID Setter function
    @id.setter 
    def id(self,id):
        self._id = id

    #titulo Getter function 
    @property    
    def titulo(self):
        return self._titulo

    #titulo Setter function
    @titulo.setter 
    def titulo(self,titulo):
        self._titulo = titulo

    #idAutor Getter function
    @property     
    def idAutor(self):
        return self._idAutor

    #idAutor Setter function
    @idAutor.setter 
    def idAutor(self,idAutor):
        self._idAutor = idAutor

    #calificacion Getter function 
    @property    
    def calificacion(self):
        return self._calificacion
      
    #calificacion Setter function
    @calificacion.setter 
    def calificacion(self,calificacion):
        self._calificacion = calificacion
         
    def __eq__(self,contribucion):
        return self.idAutor == contribucion.idAutor

    @classmethod
    def obInstances(cls):
        """
            Metodo de clase para obtener y contar las instancias realizadas
        """
        return cls.instances
        
                
        
            
            
        