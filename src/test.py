import locale
import calendar
from datetime import *
from Funciones import *
from Electricidad import *

locale.setlocale(locale.LC_ALL,'es_ES.utf8')
def obtener_datos():
    # estos datos en vez de crear un objeto electricidad se cogerían de la base de datos pero ahora estamos probando que funciona
    datos = {
            'precio': obtener_precio(fecha),
            'fecha': fecha,
            'precio_estimado_manana': obtener_precio_estimado(fecha + timedelta(days=1)),
            'porcentaje_de_subida_o_bajada':  obtener_porcentaje(fecha),
            'dia_semana_actual': dia_de_la_semana(fecha),
            'subida_precio': subida_precio(fecha)
        }
    return Electricidad(datos)

print("¿De que dia quieres comprobar la electricidad?(xx)")
dia = int(input())
print("¿De que mes quieres comprobar la electricidad?(xx)")
mes = int(input())
print("¿De que ano quieres comprobar la electricidad?(xxxx)")
ano = int(input())
try:
    fecha = date(ano,mes,dia)
    print(calendar.month(ano,mes,2,1))
    electricidad = obtener_datos()
    print('Se ha buscado los datos de la electricidad del', electricidad.fecha)
    print('El precio de la electricidad el dia', fecha, 'es', electricidad.precio)
    if(electricidad.porcentaje_de_subida_o_bajada >= 0):
        print('El porcentaje de subida es de', electricidad.porcentaje_de_subida_o_bajada)
    else:
        print('El porcentaje de bajada es de', electricidad.porcentaje_de_subida_o_bajada)    
    print('El precio estimado para el dia', fecha + timedelta(days=1), 'es', electricidad.precio_estimado_manana)
    print('El', fecha, 'es', electricidad.dia_semana_actual)
    if(electricidad.subida_precio):
        print('El', fecha, 'es fin de semana')
    else:
        print('El', fecha, 'no es fin de semana')
    print('El dia más barato de esta semana es el',obtener_dia_de_la_semana_mas_barato())

except:
    print('Escribe una fecha valida')

