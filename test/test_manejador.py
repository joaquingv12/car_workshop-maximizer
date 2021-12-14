import pytest
from src.manejador import *
from test.test_vehiculos import vehiculo

@pytest.fixture
def manejador():
    manejador = Manejador()
    return manejador

@pytest.fixture
def vehiculo(manejador):
    vehiculo = manejador.crear_nuevo_vehiculo('1234ABC', TipoAveria.RUEDA_PINCHADA, 5)
    assert vehiculo is not None
    return vehiculo

@pytest.fixture
def reparacion(manejador):
    v1 = Vehiculo('1234ABC', TipoAveria.RUEDA_PINCHADA, 10)
    v2 = Vehiculo('2345ABD', TipoAveria.GOLPE, 30)
    v3 = Vehiculo('2345ACD', TipoAveria.MOTOR_AVERIADO, 60)
    v4 = Vehiculo('4345ACD', TipoAveria.BATERIA_GASTADA, 5)
    listado_vehiculos = [v1, v2, v3, v4]
    reparacion = manejador.crear_nueva_reparacion(listado_vehiculos,5)
    assert reparacion is not None
    return reparacion

def test_manejador_nuevo_vehiculo_reparacion(manejador,reparacion):
    nuevo_vehiculo = Vehiculo('4231CDE', TipoAveria.BATERIA_GASTADA, 5)
    manejador.añadir_nuevo_vehiculo_reparacion(reparacion,nuevo_vehiculo)
    assert len(reparacion.listado_vehiculos) == 5

def test_manejador_añadir_nueva_averia_vehiculo(manejador,vehiculo):
    manejador.añadir_nueva_averia_vehiculo(vehiculo,TipoAveria.LUNA_ROTA)
    assert len(vehiculo.listado_averias) == 2
    assert vehiculo.listado_averias[1] == TipoAveria.LUNA_ROTA

def test_manejador_aniadir_fecha_salida_vehiculo(manejador,vehiculo):
    manejador.aniadir_fecha_salida_vehiculo(vehiculo, date.today())
    assert vehiculo.fecha_de_salida is not None

def test_manejador_cambiar_estado_reparacion_vehiculo(manejador,vehiculo):
    manejador.cambiar_estado_reparacion_vehiculo(vehiculo,True)
    assert vehiculo.reparado == True
