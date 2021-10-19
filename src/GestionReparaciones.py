class GestionReparaciones:
    '''Clase que se encarga de gestionar las reparaciones de los vehículos '''
    def __init__(self, vehiculos_reparar, puestos_reparacion):
        '''
        Constructor de la clase.

            Atributos
            ---------
            vehiculos_reparar : lista de objetos vehiculos
                    Vehículos que tienen que ser reparados
            puestos_reparacion : int
                    Número de puestos de reparación disponibles en el taller.
        '''
        self.vehiculos_reparar = vehiculos_reparar
        self.puestos_reparacion = puestos_reparacion
    
    