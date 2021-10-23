from datetime import *
import enum


class TipoAveria(enum.Enum):
    '''
    Enumerado
    ----------
    '''
    GOLPE = 1
    RUEDA_PINCHADA = 2
    

class Vehiculo:
    '''
    Atributos
    ----------
    matricula : float
        Matrícula del vehículo
    tipo_averia : TipoAveria
        Tipo de averia que tiene el vehiculo
    fecha_de_llegada : Date
        Fecha en la que el vehículo llega al taller
    fecha_de_salida: Date
        Fecha en la que el vehículo sale del taller
    tiempo_estimado_reparacion : float
        Tiempo estimado para la reparación del vehículo
    reparado : boolean
        true si está reparado, false si está averiado
    '''
    def __init__(self, matricula,  tipo_averia):
        ''' Inicializa los atributos de la clase '''
        self.matricula = matricula
        self.tipo_averia = tipo_averia
        self.fecha_de_llegada = datetime.today()
        self.fecha_de_salida = None
        self.reparado = False
    def obtener_matricula(self):
        ''' Devuelve la matricula del vehículo '''
        return self.matricula
    def obtener_fecha_llegada(self):
        ''' Devuelve la fecha de llegada del vehículo '''
        return self.fecha_de_llegada
    def obtener_tiempo_estimado_reparacion(self):
        ''' Devuelve un tiempo estimado de reparación '''
        return self.tiempo_estimado_reparacion
    def obtener_fecha_de_salida(self):
        ''' Devuelve la fecha de salida del vehículo '''
        return self.fecha_de_salida
    def fecha_de_salida(self,fecha_de_salida):
        ''' Añade la fecha de salida del vehículo '''
        self.fecha_de_salida = fecha_de_salida
    def obtener__reparado(self):
        ''' Añade la fecha de salida del vehículo '''
        return self.reparado