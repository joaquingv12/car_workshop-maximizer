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
El gestor de tareas que voy a utilizar para el proyecto es **Invoke**, que es un gestor de tareas para Python. Se encuentra en el archivo [tasks](tasks.py), éste contiene las tareas básicas del proyecto, entre ellas:
* `invoke install`
* `invoke installdeps`
* `invoke test`
* `invoke check --f <nombre_clase>`

Para ver todas las tareas disponibles: `invoke --list`
![](/docs/imagenes/invoke_list.png)
***
## Clase GestionReparaciones

Clase encargada de gestionar los vehículos averíados del taller para cada día en los puesto de reparación. Almacenará los vehículos que se tienen que reparar además de los puestos de reparación que tiene disponibles el taller. Su uso dentro del servicio se basará en que realizará una distribución de los vehículos según el tiempo necesario para arreglar sus averías en los distintos puestos de trabajo para que en su global el taller realice el mayor número de reparaciones posibles en el menor tiempo posible.

Para instalarla y comprobar la sintaxis se hará uso de la orden check :
`invoke install check --f GestionReparaciones`

***
## Documentación adicional
* [Configuración de git](docs/configurar_git.md)
  