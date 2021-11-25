#Contenedor base
FROM python:3.8-slim-buster
LABEL version="1.0.0" maintainer="joaquingv12@gmail.com"

# Directorio donde trabajar inicialmente para instalar dependencias y task runner
WORKDIR /app/

# Ficheros necesarios para el gestor de dependencias
COPY poetry.lock pyproject.toml ./ 

# Instalar gestor de dependencias
RUN pip install poetry \
    && poetry config virtualenvs.create false 

# Instalar dependencias necesarias para realizar los test
RUN poetry install

#Directorio en el que trabajar para ejecutar los test
WORKDIR /app/test

# Ejecutar los test
ENTRYPOINT ["invoke", "test"]