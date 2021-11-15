#Contenedor base
FROM python:3.8-slim 
LABEL version="1.0.0" maintainer="joaquingv12@gmail.com"

# Directorio donde trabajar
WORKDIR /app/test

# Instalar task runner
RUN pip install invoke
# Archivo con las tareas
COPY tasks.py ./

# Ficheros necesarios para el gestor de dependencias
COPY poetry.lock pyproject.toml ./ 
# Instalar gestor de dependencias
RUN  pip install poetry && poetry config virtualenvs.create false 

# Instalar dependencias necesarias para realizar los test
RUN invoke installdeps

# Ejecutar los test
CMD ["invoke", "test"]