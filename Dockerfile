#Contenedor base
FROM python:3.8-alpine
LABEL version="1.0.0" maintainer="joaquingv12@gmail.com"

# Directorio donde trabajar
WORKDIR /app/

#Instalo el compilador de C y el shell de bash para que funcione Invoke
RUN apk update \
    && apk upgrade \
    && apk add gcc musl-dev libffi-dev \
    && apk add bash


# Ficheros necesarios para el gestor de dependencias y el gestor de tareas
COPY tasks.py poetry.lock pyproject.toml ./ 

# Instalar task runner y gestor de dependencias
RUN pip install invoke \
    && pip install poetry \
    && poetry config virtualenvs.create false 

# Instalar dependencias necesarias para realizar los test
RUN invoke installdeps

# Ejecutar los test
CMD ["invoke", "test"]