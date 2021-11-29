# -*- coding: utf-8 -*-
import pytest
from src.Reparaciones import *
from src.Vehiculo import *

@pytest.fixture
def reparaciones():
    v1 = Vehiculo('1234ABC', TipoAveria.RUEDA_PINCHADA, 10)
    v2 = Vehiculo('2345ABD', TipoAveria.GOLPE, 30)
    v3 = Vehiculo('2345ACD', TipoAveria.MOTOR_AVERIADO, 60)
    v4 = Vehiculo('4345ACD', TipoAveria.BATERIA_GASTADA, 5)
    listado_vehiculos = [v1, v2, v3, v4]
    reparaciones = Reparaciones(listado_vehiculos, 3)    
    return reparaciones

def test_lista_distribucion_vacia_al_crearlo(reparaciones):
    assert len(reparaciones.lista_distribucion) == reparaciones.puestos_de_reparacion
    for i in reparaciones.lista_distribucion:
        assert len(i) == 0

def test_añadir_nuevo_vehiculo(reparaciones):
    nuevo_vehiculo = Vehiculo('4231CDE', TipoAveria.BATERIA_GASTADA, 5)
    reparaciones.añadir_nuevo_vehiculo(nuevo_vehiculo)
    assert len(reparaciones.listado_vehiculos) == 5


