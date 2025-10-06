# Usa una imagen base de Python 3.12 slim (versión ligera)
FROM python:3.12-slim

# Información sobre el contenedor (metadata)
LABEL maintainer="jhoanc@sistemas.edu.co"
LABEL description="API REST de Gestión de Tareas con Flask"
LABEL version="1.0"

# Crear y establecer el directorio de trabajo dentro del contenedor
# Todo lo que hagamos se ejecutará desde /app
WORKDIR /app

# COPY: Copia archivos desde tu PC al contenedor
# . : Destino (directorio actual = /app)
# Esto es una optimización: si solo cambias código, Docker reutiliza este paso
COPY requirements.txt .

# Instalar las dependencias de Python
# pip install lee el requirements.txt y descarga Flask y Werkzeug
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar TODO el código de la aplicación al contenedor
# Esto incluye app.py y cualquier otro archivo en tu carpeta
COPY . .

# Exponer el puerto 8000
# Puerto donde Flask escucha (definido en app.py)
EXPOSE 8000

# Comando que se ejecuta cuando el contenedor inicia
# Ejecuta: python app.py
CMD ["python", "app.py"]