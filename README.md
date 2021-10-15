# Proyecto-IV
## Idea del proyecto
La idea del proyecto es crear un sistema que ayude a los usuarios a tener un control sobre el consumo de la electricidad. El sistema mostrará para cada día de la semana cuándo es más probable que suba el precio o que descienda. Esto lo predecidirá teniendo en cuenta el tiempo metereológico que hará en los próximos días (dado que, por ejemplo, el viento ayuda a producir más energía eólica y abarata el precio) , la estación del año, el día de la semana o teniendo en cuenta las horas puntas del consumo eléctrico. Esto ayudará a los usuarios a reducir el precio de su factura de la luz ya que podrán organizar las tareas que requieran mayor consumo eléctrico los días que se han predecido como más baratos.

## Historias de usuario
* [HU1](https://github.com/joaquingv12/Proyecto-IV/issues/4)
* [HU2](https://github.com/joaquingv12/Proyecto-IV/issues/3)
* [HU3](https://github.com/joaquingv12/Proyecto-IV/issues/6)

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
  