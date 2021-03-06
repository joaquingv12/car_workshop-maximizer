# CarWorkshopMaximizer

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
* `invoke rundocker`

Para ver todas las tareas disponibles: `invoke --list`
![imagen con las opciones disponibles](/docs/imagenes/invoke_list.png)

## Gestor de dependencias

He decidido utilizar el gestor de dependencias Poetry para el proyecto, para ello, se ha instalado siguiendo la [documentacion](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) de su web.

Los pasos a seguir **en Linux** son:

    pip install poetry
    poetry config virtualenvs.create false 

***

## Clase Reparaciones

Clase encargada de gestionar los vehículos averíados del taller para cada día en los puesto de reparación. Almacenará los vehículos que se tienen que reparar además de los puestos de reparación que tiene disponibles el taller. Su uso dentro del servicio se basará en que realizará una distribución de los vehículos según el tiempo necesario para arreglar sus averías en los distintos puestos de trabajo para que en su global el taller realice el mayor número de reparaciones posibles en el menor tiempo posible.

Para instalarla y comprobar la sintaxis se hará uso de la orden check :
`invoke install check`

***

## Marco de tests

Para llevar a cabo la realización de los tests, he elegido el marco de test __Pytest__. A diferencia de unittest, que para cada archivo de test hay que crear una clase que herede de TestCase, en Pytest no es necesario crear ninguna clase. En cuanto a la __biblioteca de aserciones__ para comprobar que un resultado es el esperado simplemente hay que usar la palabra clave `assert`, mientras que en otros marcos de test hay que especificar el tipo de aserción, por ejemplo, `assertTrue` para comprobar que una sentencia es evaluada como True.

Además, __Pytest__ permite el uso de *fixtures*, estos son funciones que permiten crear objetos antes de ejecutar cada función de los test cuando se pasa como parámetro un objeto con el mismo nombre que el de la función *fixture*. De esta forma, si en una función del test modificamos el objeto creado en la función fixture, no hay que preocuparse en los demás test, ya que el objeto se vuelve a configurar antes de cada función test.

Para ejecutar los tests se puede usar el comando `pytest` o directamente con el task runner `invoke install test`. Los tests creados se encuentran en [esta carpeta](test).

***

## Contenedor
Para poder desplegar el proyecto en un servidor en la nube, se ha utilizado  **Docker**. Como **contenedor base** he utilizado el **oficial del lenguaje de programación Python**, pero la **versión 3.8:slim-buster**.

**1. Requisitos**
   1. Versión de Python 3.8, ya que es la versión de Python que estoy utilizando para desarrollar el proyecto.
   2. Que sea una imagen oficial.
   3. Que esté mantenida actualmente.
   4. Versión ligera, ya que sólo es necesario para pasar los tests.
   5. Tiene que tener instalado el compilador gcc y el shell de bash para que funcione Invoke.

**2. Parámetros de la búsqueda**
Tras hacer una búsqueda, las imágenes que cumplen estos requisitos son: python:3.8-slim, python:3.8-slim-buster y python:3.8-slim-bullseye. He descartado la versión alpine, a pesar de ser la más ligera, porque he leído en varias webs, como por ejemplo, [ejemplo1](https://pythonspeed.com/articles/alpine-docker-python/), [ejemplo2](https://pythonspeed.com/articles/base-image-python-docker-images/) que no es muy recomendable.

**3. Pruebas**
Tras hacer pruebas con cada uno de ellos, he obtenido los siguientes tamaños de imaǵenes:
| Imagen        | Tamaño |
|---------------|--------|
| slim          | 181 MB |
| slim-buster   | 173 MB |
| slim-bullseye | 181 MB |

Como con todas ellas, funcionan correctamente los test, voy a usar la que menos tamaño ocupa a pesar de que la diferencia no es muy notable ya que también ayuda a que el contenedor se baje de forma rápida sin necesidad de perder mucho tiempo para pasar los test.

Para crear este contenedor, he utilizado el siguiente [Dockerfile](Dockerfile) que contiene la configuración de la imagen que se va a desplegar, entre esta configuración se encuentra, como ya he dicho, el uso de la versión slim-buster de Python, `python:3.8-slim-buster`. A la hora de construir el contenedor, para instalar las dependencias necesarias para los test, hace uso de Poetry y una vez construido, para pasar los test, uso el ENTRYPOINT, que permite especificar el ejecutable que va a usar el contenedor, concretamente `invoke test`.

Este contenedor se encuentra publicado en DockerHub, en [joaquingv12/car_workshop-maximizer](https://hub.docker.com/r/joaquingv12/car_workshop-maximizer).

Para correr el contenedor y que ejecute los test hay que hacer:

    invoke rundocker

***
## Sistemas de integración continua
Para la integración continua voy a usar una GitHub Action y además, usaré otro sistema online. La GitHub Action que voy a usar es la que se encuentra en el siguiente [fichero](.github/workflows/test_app.yml), el cual está dentro de la carpeta *.github/workflows*

Aparte de las GitHub Actions se necesita un sistema online que sea estándar y flexible para poder hacer integración continua, las diferentes opciones son las siguientes (entre otras muchas):
* Travis CI
* Circle CI
* Semaphore CI
  
Con estas opciones, teniendo en cuenta que Travis a pesar de conectarse con GitHub Education te obligaba a elegir un plan e introducir una tarjeta de crédito, he decidido descartarlo. Entre CircleCI y SemaphoreCI, he elegido Circle CI, ya que tras un primer uso, he visto que es sencilla de configurar, con sólo elegir el lenguaje de programación ya te da una plantilla de configuración que permite crear un trabajo para pasar los test, la cual sólo hay que modificarla como queramos, y además, es obligatorio usarlo para alcanzar el objetivo de integración continua de la asignatura. También, he visitado varias webs donde he consultado la [popularidad de los sistemas de integración continua](https://www.saashub.com/best-continuous-integration-software) y queda claro que SemaphoreCI no es tan popular como CircleCI, por lo que como consecuencia sería más difícil encontrar ayuda a la hora de solucionar cualquier problema con éste. En la siguiente [web](https://www.slant.co/topics/799/~best-continuous-integration-tools) donde hay un ranking sobre los mejores sistemas de CI, CircleCI aparece justo debajo de Travis mientras que SemaphoreCI aparece mucho más abajo, siendo éste otro motivo de la elección de CircleCI.

### Configuración de Circle CI

La configuración del sistema de integración continua CircleCI se encuentra en el siguiente [fichero](.circleci/config.yml), llamado *config.yml* y que para que funcione correctamente tiene que estar dentro de la carpeta *.circleci*. Algunos aspectos relevantes de la configuración son:

**Executors**: Definen el entorno en donde se van a desarrollar los trabajos (jobs) creados en *config.yaml*. Tiene varias formas de hacerlo, tras haber probado a hacerlo con un contenedor, me he dado cuenta que no es la forma más sencilla de hacerlo, dado que debería montar mi repositorio en ese contenedor y ese a su vez debería montarlo en el contenedor creado anteriormente para los test. Por tanto, he optado por usar el executor con la opción *machine* que permite correr trabajos en una máquina virtual de entre las imágenes disponibles de la siguiente [lista de imágenes](https://circleci.com/docs/2.0/configuration-reference/#available-machine-images) , como estoy desarrollando mi proyecto en Ubuntu, he elegido la versión más reciente, `ubuntu-2004:202111-01`, que contiene Ubuntu 20.04, Docker v20.10.11, Docker Compose v1.29.2

**Steps**: Los pasos que he tenido que configurar con CircleCI para pasar los test son los siguientes:
1. Checkout
2. Cambiar a la versión 3 de Python, ya que es la que estoy utilizando para desarrollar la aplicación. Como la máquina virtual usada (ubuntu-2004:202111-01) sólo tiene dos versiones de Python instaladas, una con Python 2 y otra con Python 3, por defecto usa la versión 2 y da algunos errores como el siguiente, *Non-ASCII character '\xe3' in file... but no encoding declared*, porque tendría que añadir al inicio de cada archivo con código Python la codificación que se está usando. Como además de la versión 2, trae concretamente la versión 3.9.7, que ya sí pertenece a la versión 3 de Python y por tanto, no da problemas con los ficheros de Python, es la que usaré. Como la aplicación funciona igual con la versión 3.8 (que es la que uso localmente) que con la 3.9.7 no es necesario instalar la 3.8 así no se pierde tiempo cada vez que se van a pasar los test en instalar esa versión de Python a la imagen.
3. Instalo el task runner para llevar a cabo la tarea encargada de pasar los test en el contenedor.
4. Ejecuto la tarea que arranca el contenedor creado en el objetivo anterior y que pasa los test.

## Testear diferentes versiones de Python
Para hacer esta tarea, la he llevado a cabo a través de la GitHub Action definida en [test_app.yml](.github/workflows/test_app.yml). Localmente, estoy desarrollando la aplicación con la versión 3.8 de Python, pero he querido comprobar si era compatible con versiones anteriores, para ello he comprobado las siguientes versiones de Python:

* 3.5: Obtenía el siguiente error, *pytest (6.2.5) requires Python >=3.6*, que como deja claro, no es posible usar esa versión ni anteriores porque la versión de pytest que uso no es compatible con versiones anteriores a la versión 3.6 de Python.
* 3.6 y 3.7: Obtenía el siguiente error,  *ModuleNotFoundError: No module named 'importlib_metadata'*, por lo que tampoco era posible testear la aplicación con esas versiones dado que esas versiones no tienen el módulo importlib_metadata.

A partir de la 3.8 hasta la 3.10, que es la última versión de Python actualmente, no ha habido ningún problema. Por eso, las versiones que uso para testear son las 3.8, 3.9 y 3.10 en distintos sistemas operativos, entre ellos, Ubuntu, Windows y MacOS.
## Documentación adicional

* [Configuración de git](docs/configurar_git.md)
  