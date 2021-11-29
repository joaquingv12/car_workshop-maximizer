# -*- coding: utf-8 -*-
import pytest
from src.Vehiculo import *

@pytest.fixture
def vehiculo():
    vehiculo = Vehiculo('1234ABC', TipoAveria.RUEDA_PINCHADA, 5)
    return vehiculo

def test_tiene_fecha_de_llegada_correcta_al_crearlo(vehiculo):
    assert vehiculo.fecha_de_llegada <= date.today()

def test_vehiculo_averiado_al_crearlo(vehiculo):
    assert vehiculo.reparado == False

def test_añade_nueva_averia(vehiculo):
    vehiculo.añadir_nueva_averia(TipoAveria.LUNA_ROTA)
    assert len(vehiculo.listado_averias) == 2
    assert vehiculo.listado_averias[1] == TipoAveria.LUNA_ROTA

def test_cambiar_a_estado_reparado(vehiculo):
    vehiculo.cambiar_estado_reparacion(True)
    assert vehiculo.reparado == True

def test_cambiar_a_estado_no_reparado(vehiculo):
    vehiculo.cambiar_estado_reparacion(False)
    assert vehiculo.reparado == False

def test_cambiar_fecha_salida(vehiculo):
    vehiculo.aniadir_fecha_salida(date.today())
    assert vehiculo.fecha_de_salida == date.today()


