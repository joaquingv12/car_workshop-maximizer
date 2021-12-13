from invoke import task, run
@task
def install(ctx):
	"""
	Instalación de las clases.
	"""
	installdeps(ctx)
	run("python src/*.py")

@task
def installdeps(ctx):  
	"""
	Instala las dependencias necesarias para que la aplicación funcione.
	"""  
	run("poetry install")

@task
def test(ctx):
	"""
	Comprueba que el código funciona correctamente.
	"""
	run("pytest -p no:logging")

@task
def check(ctx):
	"""
	Comprueba que la sintaxis es correcta.
	"""
	try:
		run("pyflakes src/*.py")
		print("Sintaxis correcta")
	except:
		print("Sintaxis incorrecta")

@task
def rundocker(ctx):
	"""
	Comprueba que el código funciona correctamente.
	"""
	try:
		run("docker run -t -v `pwd`:/app/test joaquingv12/car_workshop-maximizer")
	except:
		run("docker run -e ETCD_PORT=${ETCD_PORT} LOG_FILE=${LOG_FILE} LOG_LEVEL=${LOG_LEVEL} -t -v `pwd`:/app/test joaquingv12/car_workshop-maximizer")
