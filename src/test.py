import locale
import calendar
from datetime import *
from Calendario import *

locale.setlocale(locale.LC_ALL,'es_ES.utf8')

print("¿De que dia quieres comprobar la electricidad?(xx)")
dia = int(input())
print("¿De que mes quieres comprobar la electricidad?(xx)")
mes = int(input())
print("¿De que ano quieres comprobar la electricidad?(xxxx)")
ano = int(input())
try:
    fecha = date(ano,mes,dia)
    print(calendar.month(ano,mes,2,1))
    calendario = Calendario(30,fecha) # 30 es un valor inventado, tendría que obtenerse de alguna manera el precio de la electricidad en esa fecha
    print('Se ha buscado los datos de la electricidad del', calendario.obtener_fecha())
    print('El precio de la electricidad el dia', fecha, 'es', calendario.obtener_precio())
    if(calendario.obtener_porcentaje() >= 0):
        print('El porcentaje de subida es de', calendario.obtener_porcentaje())
    else:
        print('El porcentaje de bajada es de', calendario.obtener_porcentaje())    
    print('El precio estimado para el dia', calendario.obtener_fecha() + timedelta(days=1), 'es', calendario.obtener_precio_estimado_manana())
    print('El', calendario.obtener_fecha(), 'es', calendario.dia_de_la_semana())
    if(calendario.fin_de_semana_o_fiesta):
        print('El', calendario.obtener_fecha(), 'es fin de semana o fiesta')
    else:
        print('El', calendario.obtener_fecha(), 'no es fin de semana o no es fiesta')
    print('El dia más barato de esta semana es el', calendario.obtener_dia_de_la_semana_mas_barato())
except:
    print('Escribe una fecha valida')
