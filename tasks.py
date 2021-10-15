from invoke import task, run
@task
def install(ctx):
	"""
	Instalación de las clases.
	"""
	installdeps(ctx)
	print("No implementado")

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

@task(help={"fichero":"fichero al que comprobar la sintaxis"})
def check(ctx,fichero):
	"""
	Comprueba que la sintaxis es correcta.
	"""
	run(f"python {fichero}")
