# Proyecto-IV
## Idea del proyecto
La idea de este proyecto es crear un sistema que ayude a los talleres de vehículos a organizar las reparaciones en los distintos puesto de reparación de los que consta el taller de forma que se optimice el uso de cada uno de ellos para acabar en el menor tiempo posible con las reparaciones y así poder reparar más vehículos cada día aumentando sus beneficios. Para esto, se tendrá en cuenta el número de vehículos que tienen que reparar así como el tipo de reparación que necesitan para tener una estimación del tiempo que tardaría en repararse cada uno. Una vez, con estos datos, a través de un algoritmo de backtracking , se obtendrá un listado de los vehículos que se tienen que reparar en cada puesto cada día para repararlos en el menor tiempo posible. Además, cada propietario de cada vehículo podrá consultar en el sistema cuando será reparado su vehículo de forma que no tenga que llamar cada día al taller para ver si va a tardar mucho en repararlo o no.

### Ejemplo del funcionamiento esperado del sistema
Si en el taller para un determinado día hay 3 puestos de reparación disponibles y 5 vehículos que reparar con los siguientes tiempos estimados de reparación según la avería: 
* __vehículo 1__ : 7 mins 
* __vehículo 2__ : 13 mins
* __vehículo 3__ : 21mins 
* __vehículo 4__ : 21 mins
* __vehículo 5__ : 24 mins
  
La forma óptima de repararlo sería:
* puesto 1 -> reparar vehículo 1 y 3 = 28mins
* puesto 2 -> reparar vehículo 2 y 4 = 34 mins
* puesto 3 -> vehículo 5 = 21 mins

De esta forma, el total de tiempo empleado sería 34 mins, mientras que de cualquier otra organización los empleados tardarían más en reparar los vehículos. 

***
## Historias de usuario
* [HU1](https://github.com/joaquingv12/Proyecto-IV/issues/13)
* [HU2](https://github.com/joaquingv12/Proyecto-IV/issues/14)
* [HU3](https://github.com/joaquingv12/Proyecto-IV/issues/15)
* [HU4](https://github.com/joaquingv12/Proyecto-IV/issues/16)

### Perfil de los usuarios

* [Perfil usuarios](docs/perfil_usuarios.md)
***
## Gestor de tareas
El gestor de tareas que voy a utilizar para el proyecto es **Invoke**, que es un gestor de tareas para Python. Se encuentra en el archivo [tasks](tasks.py), éste contiene las tareas básicas del proyecto, entre ellas:
* `invoke install`
* `invoke installdeps`
* `invoke test`
* `invoke check`

Para ver todas las tareas disponibles: `invoke --list`
![](/docs/imagenes/invoke_list.png)
***
## Clase Reparaciones

Clase encargada de gestionar los vehículos averíados del taller para cada día en los puesto de reparación. Almacenará los vehículos que se tienen que reparar además de los puestos de reparación que tiene disponibles el taller. Su uso dentro del servicio se basará en que realizará una distribución de los vehículos según el tiempo necesario para arreglar sus averías en los distintos puestos de trabajo para que en su global el taller realice el mayor número de reparaciones posibles en el menor tiempo posible.

Para instalarla y comprobar la sintaxis se hará uso de la orden check :
`invoke install check `

***

## Marco de tests
Para llevar a cabo la realización de los tests, he elegido el marco de test __Pytest__. A diferencia de unittest, que para cada archivo de test hay que crear una clase que herede de TestCase, en Pytest no es necesario crear ninguna clase. En cuanto a la __biblioteca de aserciones__ para comprobar que un resultado es el esperado simplemente hay que usar la palabra clave `assert`, mientras que en otros marcos de test hay que especificar el tipo de aserción, por ejemplo, `assertTrue` para comprobar que una sentencia es evaluada como True. 

Además, __Pytest__ permite el uso de *fixtures*, estos son funciones que permiten crear objetos antes de ejecutar cada función de los test cuando se pasa como parámetro un objeto con el mismo nombre que el de la función *fixture*. De esta forma, si en una función del test modificamos el objeto creado en la función fixture, no hay que preocuparse en los demás test, ya que el objeto se vuelve a configurar antes de cada función test.

Para ejecutar los tests se puede usar el comando `pytest` o directamente con el task runner `invoke install test`. Los tests creados se encuentran en [esta carpeta](test).

***
## Documentación adicional
* [Configuración de git](docs/configurar_git.md)
  