# -*- coding: utf-8 -*-
from datetime import *
import enum

class TipoAveria(enum.Enum):
    '''
    Enumerado
    ----------
    Permite clasificar los tipos de averías que tiene cada vehículo cuando llega al taller. 
    '''
    GOLPE = 1
    RUEDA_PINCHADA = 2
    LUNA_ROTA = 3
    MOTOR_AVERIADO = 4
    BATERIA_GASTADA = 5

class Vehiculo:
    '''
    Clase que contiene la información de cada vehículo averiado.

    Atributos
    ----------
    matricula : str
        Matrícula del vehículo
    tipo_averias : [TipoAveria]
        Listado con el tipo de averias que tiene el vehiculo
    fecha_de_llegada : Date
        Fecha en la que el vehículo llega al taller
    fecha_de_salida: Date
        Fecha en la que el vehículo sale del taller
    tiempo_estimado_reparacion : int
        Tiempo estimado (minutos) para la reparación del vehículo
    reparado : boolean
        true si está reparado, false si está averiado
    '''
    def __init__(self, matricula, listado_averias, tiempo_estimado_reparacion):
        ''' Inicializa los atributos de la clase '''

        #Validar los datos introducidos
        if type(matricula) != str or len(matricula) <= 3: #La mayoría de las matrículas tienen al menos 4 caracteres
            raise TypeError("Matrícula incorrecta")

        if type(listado_averias) != list:
            listado_averias = [listado_averias]
        
        for averia in listado_averias:
            if type(averia) != TipoAveria:
                listado_averias.remove(averia) #No añadir las averías que no son correctas
        
        if type(tiempo_estimado_reparacion) != int:
            raise TypeError("Tiempo estimado de reparación tiene que ser un entero")
        
        if tiempo_estimado_reparacion <= 0:
            raise ValueError("El tiempo estimado de reparación tiene que ser mayor a 0")

        self.matricula = matricula
        self.listado_averias = listado_averias
        self.tiempo_estimado_reparacion = tiempo_estimado_reparacion
        self.fecha_de_llegada = date.today()
        self.fecha_de_salida = None
        self.reparado = False
 

    def aniadir_fecha_salida(self,fecha_de_salida):
        ''' Añade la fecha de salida del vehículo '''
        if not isinstance(fecha_de_salida,date):
            raise TypeError("El formato de la fecha de salida no es correcto")
        self.fecha_de_salida = fecha_de_salida

    def añadir_nueva_averia(self,nueva_averia):
        ''' Añade una nueva avería al vehículo '''
        if type(nueva_averia) != TipoAveria:
            raise TypeError("El tipo de avería no es correcto")
        self.listado_averias.append(nueva_averia)
    
    def cambiar_estado_reparacion(self, reparado):
        ''' Cambia el estado de reparación del vehículo '''
        self.reparado = reparado
