
# API REST con Flask + Docker

Esta aplicación es una API REST básica desarrollada con Flask y ejecutada dentro de un contenedor Docker. 
El `Dockerfile` usa una imagen base ligera de **Python 3.12-slim**, instala las dependencias definidas en `requirements.txt` (Flask y Werkzeug), 
copia el código fuente y expone el puerto **8000**, donde la aplicación Flask se ejecuta mediante `python app.py`.
El contenedor aísla completamente el entorno de ejecución, garantizando portabilidad y evitando conflictos locales. 
Al desplegarse, el servidor Flask escucha en `0.0.0.0:8000`, permitiendo el acceso desde cualquier equipo o servicio en la nube, como Render.com.
