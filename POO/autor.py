import re

class Autor:
    """Clase que representa al Autor"""
    def __init__(self): #self, id = int, nombre = str, universidad= str, email=str, calificacion=[], publicaciones=int):
        self.id= 0
        self.nombre = ""
        self._universidad= ""
        self._email = ""
        #self.calificacionMaxima = max(calificacion)
        self.cantPublicaciones= 0
        #self.promedioCalificacion= calcularPromedio(calificacion)

    def verificarCalificacion(self):
        pass
    
    def calcularPromedio(self,calificacion):
        pass
    
    @property    #ID Getter function 
    def id(self):
        return self._id

    @id.setter #ID Setter function
    def id(self,id = int):
        self._id = id

    @property    #Nombre Getter function 
    def nombre(self):
        return self._nombre

    @nombre.setter #Nombre Setter function
    def nombre(self,nombre = str):
        self._nombre = nombre

    @property    #Email Getter function 
    def email(self):
        return self._email

    @email.setter #Email Setter function
    def email(self,email = str):
        pattern = re.compile(r"[\w\._]{1,30}@[\w\.\-]+\.[a-z]{2,5}")
        res = re.match(pattern,email)
        if res:
            self._email = email
        else:
            self._email ="Ingrese un correo válido"
        
    @property    #universidad Getter function 
    def universidad(self):
        return self._universidad

    @universidad.setter #universidad Setter function
    def universidad(self,universidad = str):
        self._universidad = universidad
