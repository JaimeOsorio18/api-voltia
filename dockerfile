# Utiliza una imagen base de Python
FROM python:3.11.2

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt /code/

# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copia el código fuente de Django al contenedor
COPY . /code/

# Define las variables de entorno para la configuración de Django
# ENV DJANGO_SETTINGS_MODULE=myproject.settings
# ENV PYTHONUNBUFFERED=1

# Expone el puerto 8000 para que pueda ser accedido desde el host
EXPOSE 8000

# Ejecuta el comando para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]