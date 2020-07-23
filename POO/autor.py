import re
from contribucion import Contribucion

class Autor:
    """Clase que representa al Autor"""
    def __init__(self, id=int, nombre='*', universidad='*', email='*', listcal=[]):
       self.id= id
       self.nombre = nombre
       self.universidad= universidad
       self._email = email
       self.calificacionMax = 0
       self.publicaciones= 0
       self.listcal=listcal
       self.promedioCalificacion= 0
        

    def verificarCalificacion(self, contribucion):
        if self.id == contribucion.idAutor:
            self._publicaciones +=1
            self._listcal.append(contribucion.calificacion)
            self._calificacionMax=max(self._listcal)
            


    def calcularPromedio(self):
        mean= sum(self._listcal) / len(self._listcal)
        self._promedioCalificacion = mean

    #ID Getter function 
    @property    
    def id(self):
        return self._id

    #ID Setter function
    @id.setter
    def id(self,id):
        self._id = id

    #Nombre Getter function 
    @property    
    def nombre(self):
        return self._nombre

    #Nombre Setter function
    @nombre.setter 
    def nombre(self,nombre):
        self._nombre = nombre

    #Email Getter function 
    @property    
    def email(self):
        return self._email

    #Email Setter function
    @email.setter 
    def email(self,email):
        pattern = re.compile(r"[\w\._]{1,30}@[\w\.\-]+\.[a-z]{2,5}")
        res = re.match(pattern,email)
        if res:
            self._email = email
        else:
            self._email ="Ingrese un correo válido"
        
    #universidad Getter function 
    @property   
    def universidad(self):
        return self._universidad

   #universidad Setter function
    @universidad.setter 
    def universidad(self,universidad):
        self._universidad = universidad


    #publicaciones Getter function 
    @property    
    def publicaciones(self):
        return self._publicaciones

    #publicaciones Setter function
    @publicaciones.setter 
    def publicaciones(self,publicaciones):
        self._publicaciones = publicaciones

    #listcal Getter function 
    @property    
    def listcal(self):
        return self._listcal

    #listcal Setter function
    @listcal.setter
    def listcal(self,listcal):
        self._listcal = listcal

    #calificacionMax Getter function 
    @property    
    def calificacionMax(self):
        return self._calificacionMax

    #calificacionMax Setter function
    @calificacionMax.setter
    def calificacionMax(self,calificacionMax):
        self._calificacionMax = calificacionMax

    #promedioCalificacion Getter function 
    @property    
    def promedioCalificacion(self):
        return self._promedioCalificacion

    #promedioCalificacion Setter function
    @promedioCalificacion.setter
    def promedioCalificacion(self,promedioCalificacion):
        self._promedioCalificacion = promedioCalificacion