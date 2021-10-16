import random
from datetime import *

# Se tendrá que buscar alguna forma de obtener el precio de la electricidad en esa fecha
def obtener_precio(fecha):
    #return round(random.SystemRandom().uniform(0, 40),2)
    return 30 # pongo un numeor exacto para que calcule bien el porcentaje pero tendria que acceder a la base de datos

# Se tendrá que crear alguna forma de estimacion (con el viento, la temperatura) para la fecha pasada(el dia sigueinte)
def obtener_precio_estimado(fecha_dia_siguiente):
    return round(random.SystemRandom().uniform(0, 40),2)

def obtener_porcentaje(fecha):
    return (obtener_precio(fecha) - 20) / 20    # siendo 20 el precio del dia anterior

def dia_de_la_semana(fecha):
    return fecha.strftime('%A')

def subida_precio(fecha):
    if( fecha.strftime('%A') == 'Saturday' or fecha.strftime('%A') == 'Sunday'):
            return True
    # o si es fiesta tambien devolvería True (Hay que buscar una forma de saber si es fiesta)
    return False

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

def obtener_dia_de_la_semana_mas_barato():
    dia_actual = datetime.today().isoweekday()
    dia_semana = dia_actual + 1
    dia_mas_barato = datetime.today()
    precio_mas_barato = obtener_precio(dia_mas_barato)
    while(dia_semana <= 7 ):
        dia_semana = datetime.today() + timedelta(days=(dia_semana-dia_actual))
        precio_dia_semana = obtener_precio(dia_semana)
        if(precio_mas_barato > precio_dia_semana):
            precio_mas_barato = precio_dia_semana
            dia_mas_barato = dia_semana

    return dia_de_la_semana(dia_mas_barato.date())
