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
	run("pip install -r requirements.txt")

@task
def test(ctx):
	"""
	Comprueba que el código funciona correctamente.
	"""
	print("No implementado")

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
