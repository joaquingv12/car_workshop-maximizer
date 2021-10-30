from datetime import *
import enum

class TipoAveria(enum.Enum):
    '''
    Enumerado
    ----------
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
    tipo_averia : TipoAveria
        Tipo de averia que tiene el vehiculo
    fecha_de_llegada : Date
        Fecha en la que el vehículo llega al taller
    fecha_de_salida: Date
        Fecha en la que el vehículo sale del taller
    tiempo_estimado_reparacion : int
        Tiempo estimado (minutos) para la reparación del vehículo
    reparado : boolean
        true si está reparado, false si está averiado
    '''
    def __init__(self, matricula, tipo_averia, tiempo_estimado_reparacion):
        ''' Inicializa los atributos de la clase '''

        #Validar los datos introducidos
        if type(matricula) != str or len(matricula) != 7:
            raise TypeError("Matrícula incorrecta")

        if type(tipo_averia) != TipoAveria:
            raise TypeError("Tipo de avería no es correcto")

        if type(tiempo_estimado_reparacion) != int:
            raise TypeError("Tiempo estimado de reparación tiene que ser un entero")
        
        if tiempo_estimado_reparacion <= 0:
            raise ValueError("El tiempo estimado de reparación tiene que ser mayor a 0")

        self.matricula = matricula
        self.tipo_averia = tipo_averia
        self.tiempo_estimado_reparacion = tiempo_estimado_reparacion
        self.fecha_de_llegada = date.today()
        self.fecha_de_salida = None
        self.reparado = False
 

    def aniadir_fecha_salida(self,fecha_de_salida):
        ''' Añade la fecha de salida del vehículo '''
        if not isinstance(fecha_de_salida,date):
            raise TypeError("El formato de la fecha de salida no es correcto")
        self.fecha_de_salida = fecha_de_salida
    
    def cambiar_estado_reparacion(self, reparado):
        ''' Cambia el estado de reparación del vehículo '''
        self.reparado = reparado
