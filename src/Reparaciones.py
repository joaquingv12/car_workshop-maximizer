from src.Vehiculo import *

class Reparaciones:
    '''
    Clase que gestiona las reparaciones de los vehículos del taller para cada día.

    Atributos
    ----------
    listado_vehiculos : [Vehiculo]
        Listado de los vehículos que se pretenden reparar
    puestos_de_reparacion : int
        Número de puestos de reparación que hay en el taller
    lista_distribucion : [[Vehiculo]]
        Lista con varias listas de vehículos, una para cada puesto del taller
    '''
    
    def __init__(self, listado_vehiculos, puestos_de_reparacion):
        ''' Inicializa los atributos de la clase '''

        #Validar los datos introducidos
        for v in listado_vehiculos:
            if type(v) != Vehiculo:
                raise TypeError("El listado tiene que ser de objetos vehículos")
        
        if puestos_de_reparacion < 0:
            raise ValueError("El número de puestos de reparación no puede ser negativo")

        self.listado_vehiculos = listado_vehiculos
        self.puestos_de_reparacion = puestos_de_reparacion
        self.lista_distribucion = [[] for i in range(puestos_de_reparacion)]
    

    def distribuir_vehiculos():
        ''' Distribuye los vehiculos en los puestos de reparación '''
    
    def obtener_listado_distribucion():
        ''' Devuelve el listado de los vehiculos ya distribuidos '''
    
    def tiempo_estimado_terminar_reparaciones():
        ''' Devolvera el tiempo estimado para terminar todas las reparaciones del día '''


