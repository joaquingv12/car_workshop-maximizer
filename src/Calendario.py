import random
from datetime import *

class Calendario:
    def __init__(self,precio_electricidad,fecha):
        self.precio_electricidad = precio_electricidad
        self.fecha = fecha
    def obtener_precio(self):
        return self.precio_electricidad
    def obtener_fecha(self):
        return self.fecha
    # Se tendrá que crear alguna forma de estimacion (con el viento, la temperatura) para la fecha pasada(el dia sigueinte)
    def obtener_precio_estimado_manana(self):
        return round(random.SystemRandom().uniform(0, 40),2)
    # Se tendrá que sustituir el numero 20 por el precio del dia anterior
    def obtener_porcentaje(self):
        return (self.precio_electricidad - 20) / 20    # siendo 20 el precio del dia anterior
    def dia_de_la_semana(self):
        return self.fecha.strftime('%A')
    def fin_de_semana_o_fiesta(self):
        if( self.fecha.strftime('%A') == 'Saturday' or self.fecha.strftime('%A') == 'Sunday'):
                return True
        # o si es fiesta tambien devolvería True (Hay que buscar una forma de saber si es fiesta)
        return False
    def obtener_dia_de_la_semana_mas_barato(self):
        dia_actual = self.fecha.isoweekday()
        dia_semana = dia_actual + 1
        dia_mas_barato = self.fecha
        precio_mas_barato = self.obtener_precio() # empieza obteniendo el precio de hoy al meterse en el while los compara con los dias que quedan de la semana
        while(dia_semana <= 7 ):
            precio_dia_semana = 1 # este precio se buscaria depende del dia de la semana en las instancias de calendario
            if(precio_mas_barato > precio_dia_semana): # si es el mismo precio, te devuelve el dia más proximo
                precio_mas_barato = precio_dia_semana
                dia_mas_barato = self.fecha + timedelta(days=(dia_semana-dia_actual))
            dia_semana += 1

        return dia_mas_barato
    # Cuando esten almacenados los datos, se tendría que recoger todos los precios del mes y dividirlo entre el numero de días
    def obtener_precio_medio_mes(self):
        return self.obtener_precio()
    # Se tendrá que buscar alguna forma de obtener el tiempo en tu localizacion
    def obtener_temperatura():
        return random.randint(-5, 45)
    # Se tendrá que buscar alguna forma de obtener el nivel de tiempo en tu localizacion
    def obtener_viento():
        # 29 a 38	Fresquito (Brisa fresca)
        # 39 a 49	Fresco (Brisa fuerte)
        # 50 a 61	Frescachón (Viento fuerte)
        # 62 a 74	Temporal (Viento duro)
        return random.randint(29, 74)
        
    