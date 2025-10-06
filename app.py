"""
API REST básica con Flask + Docker
Autor: Sistema de gestión de tareas
Fecha: 2025
Descripción: Versión simplificada de la API de Tareas con endpoints principales
"""

from flask import Flask, jsonify
from datetime import datetime

# Inicializar aplicación Flask
app = Flask(__name__)

# Base de datos simulada en memoria
tasks = [
    {
        "id": 1,
        "titulo": "Completar trabajo de Docker",
        "descripcion": "Crear API con Flask y desplegarla en contenedor Docker",
        "completada": False,
        "fecha_creacion": "2025-10-06"
    },
    {
        "id": 2,
        "titulo": "Estudiar para examen de sistemas",
        "descripcion": "Repasar contenedores, APIs y arquitectura de software",
        "completada": True,
        "fecha_creacion": "2025-10-07"
    }
]


# ==================== ENDPOINTS ====================

@app.route('/', methods=['GET'])
def home():
    """
    Endpoint raíz de bienvenida
    """
    return jsonify({
        "mensaje": "¡Bienvenido a la API de Gestión de Tareas (versión simplificada)!",
        "version": "1.0",
        "rutas_disponibles": {
            "/": "Mensaje de bienvenida",
            "/tasks": "Lista de tareas existentes"
        },
        "autor": "Api_Docker_NT"
    }), 200


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Retorna todas las tareas en formato JSON
    """
    return jsonify({
        "total_tareas": len(tasks),
        "tareas": tasks
    }), 200


# ==================== EJECUCIÓN ====================

if __name__ == '__main__':
    # host='0.0.0.0' permite que Docker exponga el puerto
    app.run(host='0.0.0.0', port=8000, debug=False)
