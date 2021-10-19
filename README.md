# Proyecto-IV
## Idea del proyecto
La idea de este proyecto es crear un sistema que ayude a los talleres de vehículos a organizar las reparaciones en los distintos puesto de reparación de los que consta el taller de forma que se optimice el uso de cada uno de ellos para acabar en el menor tiempo posible con las reparaciones y así poder reparar más vehículos cada día aumentando sus beneficios. Para esto, se tendrá en cuenta el número de vehículos que tienen que reparar así como el tipo de reparación que necesitan para tener una estimación del tiempo que tardaría en repararse cada uno. Una vez, con estos datos, a través de un algoritmo de backtracking , se obtendrá un listado de los vehículos que se tienen que reparar en cada puesto cada día para repararlos en el menor tiempo posible. Además, cada propietario de cada vehículo podrá consultar en el sistema cuando será reparado su vehículo de forma que no tenga que llamar cada día al taller para ver si va a tardar mucho en repararlo o no.

## Historias de usuario
* [HU1](https://github.com/joaquingv12/Proyecto-IV/issues/13)
* [HU2](https://github.com/joaquingv12/Proyecto-IV/issues/14)
* [HU3](https://github.com/joaquingv12/Proyecto-IV/issues/15)
* [HU4](https://github.com/joaquingv12/Proyecto-IV/issues/16)

### Perfil de los usuarios

* [Perfil usuarios](docs/perfil_usuarios.md)

## Gestor de tareas
El gestor de tareas que voy a utilizar para el proyecto es **Invoke**, que es un gestor de tareas para Python. Se encuentra en el archivo [tasks](tasks.py),éste contiene las tareas básicas del proyecto, entre ellas:
* `invoke install`
* `invoke installdeps`
* `invoke test`
* `invoke check --fichero <nombre>`

Para ver todas las tareas disponibles: `invoke --list`
![](/docs/imagenes/invoke_list.png)
***
## Clase Electricidad

Clase encargada de la información relacionada con el precio de la electricidad para cada día, esa información será usada para llevar a cabo las distintas operaciones con el precio de la luz.

Para comprobar la sintaxis se hará uso de la orden check :
`invoke check --fichero Electricidad.py`

Esta clase será usada para tener un control del precio de la luz en una determinada fecha, tendrá las funciones necesarias para obtener el precio real de un día anterior desde una web, además, junto con las funciones auxiliares que obtienen información del tiempo permitirá estimar el precio de los días siguientes.
***
## Documentación adicional
* [Configuración de git](docs/configurar_git.md)
  