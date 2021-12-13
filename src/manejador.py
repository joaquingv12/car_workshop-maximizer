try:
    from logger import *
    from Reparaciones import *
    from Vehiculo import *

except ImportError:
    from src.logger import *
    from src.Reparaciones import *
    from src.Vehiculo import *

class Manejador():
    def __init__(self):
        super().__init__()
        self.logger = logger

    def crear_nueva_reparacion(self,lista_vehiculos,puestos_reparacion):
        try:
            reparacion = Reparaciones(lista_vehiculos,puestos_reparacion)
            self.logger.info("Se ha creado una nueva reparación")
            return reparacion
        except Exception as e:
            self.logger.error("Error al crear una nueva reparación")
            raise e

    def crear_nuevo_vehiculo(self, matricula, listado_averias, tiempo_estimado_reparacion):
        try:
            vehiculo = Vehiculo(matricula, listado_averias, tiempo_estimado_reparacion)
            self.logger.info("Se ha creado un nuevo vehiculo")
            return vehiculo
        except Exception as e:
            self.logger.error("Error al crear un nuevo vehiculo")
            raise e
    
    def añadir_nuevo_vehiculo_reparacion(self, reparacion,vehiculo):
        try:
            reparacion.añadir_nuevo_vehiculo(vehiculo)
            self.logger.info("Se ha añadido un nuevo vehiculo a la reparación")
        except Exception as e:
            self.logger.error("Error al añadir un nuevo vehiculo a la reparación")
            raise e
        
    def añadir_nueva_averia_vehiculo(self, vehiculo, averia):
        try:
            vehiculo.añadir_nueva_averia(averia)
            self.logger.info("Se ha añadido una nueva averia al vehiculo")
        except Exception as e:
            self.logger.error("Error al añadir una nueva averia al vehiculo")
            raise e

    def aniadir_fecha_salida_vehiculo(self, vehiculo, fecha_salida):
        try:
            vehiculo.aniadir_fecha_salida(fecha_salida)
            self.logger.info("Se ha añadido una nueva fecha de salida al vehiculo")
        except Exception as e:
            self.logger.error("Error al añadir una nueva fecha de salida al vehiculo")
            raise e
    
    def cambiar_estado_reparacion_vehiculo(self,vehiculo,estado):
        try:
            vehiculo.cambiar_estado_reparacion(estado)
            self.logger.info("Se ha cambiado el estado de la reparación del vehiculo")
        except Exception as e:
            self.logger.error("Error al cambiar el estado de la reparación del vehiculo")
            raise e

    