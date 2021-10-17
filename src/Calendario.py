from datetime import *

class Calendario:
    def __init__(self,precio_electricidad,fecha):
        self.precio_electricidad = precio_electricidad
        self.fecha = fecha

    def obtener_precio(self):
        ''' Consultar el precio de un dia '''
        return self.precio_electricidad

    def obtener_fecha(self):
        ''' Consultar la fecha de ese precio de electricidad'''
        return self.fecha

    def obtener_porcentaje():
        ''' Conocer el porcentaje de subida o bajada con respecto el día anterior'''

    def dia_de_la_semana():
        ''' Conocer el dia de la semana de ese precio de electricidad '''

    def fin_de_semana_o_fiesta():
        ''' Conocer si es fin de semana o fiesta porque podría aumentar el precio '''

    def obtener_dia_de_la_semana_mas_barato():
        ''' Conocer cual es el dia más barato de la semana '''

    def obtener_viento():
        ''' Conocer el viento que hace ese dia ya que puede afectar al precio'''

    def obtener_estacion():
        ''' Conocer la estación del año ya que puede afectar al precio'''
        
    