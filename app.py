"""
API REST de Gestión de Tareas usando Flask
Autor: Sistema de gestión de tareas
Fecha: 2025
Descripción: API simple para crear, leer, actualizar y eliminar tareas
"""

from flask import Flask, jsonify, request
from datetime import datetime

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Base de datos en memoria (simulación)
# En producción esto estaría en una base de datos real como PostgreSQL o MongoDB
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
        "completada": False,
        "fecha_creacion": "2025-10-06"
    }
]

# Contador para IDs únicos
next_id = 3


# ==================== ENDPOINTS ====================

@app.route('/', methods=['GET'])
def home():
    """
    Endpoint de bienvenida
    Retorna información básica de la API
    """
    return jsonify({
        "mensaje": "¡Bienvenido a la API de Gestión de Tareas!",
        "version": "1.0",
        "endpoints_disponibles": {
            "GET /tasks": "Obtener todas las tareas",
            "GET /tasks/<id>": "Obtener una tarea específica",
            "POST /tasks": "Crear nueva tarea",
            "PUT /tasks/<id>": "Actualizar tarea",
            "DELETE /tasks/<id>": "Eliminar tarea"
        },
        "documentacion": "Visita /tasks para ver todas las tareas"
    }), 200


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Obtiene todas las tareas almacenadas
    Retorna: Lista JSON con todas las tareas
    """
    return jsonify({
        "total_tareas": len(tasks),
        "tareas": tasks
    }), 200


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """
    Obtiene una tarea específica por su ID
    Parámetros:
        task_id (int): ID de la tarea a buscar
    Retorna: Tarea encontrada o mensaje de error
    """
    # Buscar tarea por ID
    task = next((t for t in tasks if t["id"] == task_id), None)
    
    if task:
        return jsonify(task), 200
    else:
        return jsonify({
            "error": "Tarea no encontrada",
            "mensaje": f"No existe una tarea con ID {task_id}"
        }), 404


@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Crea una nueva tarea
    Body JSON esperado:
    {
        "titulo": "string",
        "descripcion": "string"
    }
    Retorna: Tarea creada con su ID asignado
    """
    global next_id
    
    # Validar que el request contenga JSON
    if not request.json:
        return jsonify({
            "error": "Formato inválido",
            "mensaje": "El body debe ser JSON"
        }), 400
    
    # Validar campos requeridos
    if "titulo" not in request.json:
        return jsonify({
            "error": "Campo faltante",
            "mensaje": "El campo 'titulo' es obligatorio"
        }), 400
    
    # Crear nueva tarea
    nueva_tarea = {
        "id": next_id,
        "titulo": request.json["titulo"],
        "descripcion": request.json.get("descripcion", ""),
        "completada": False,
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d")
    }
    
    tasks.append(nueva_tarea)
    next_id += 1
    
    return jsonify({
        "mensaje": "Tarea creada exitosamente",
        "tarea": nueva_tarea
    }), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Actualiza una tarea existente
    Parámetros:
        task_id (int): ID de la tarea a actualizar
    Body JSON (opcional):
    {
        "titulo": "string",
        "descripcion": "string",
        "completada": boolean
    }
    Retorna: Tarea actualizada o mensaje de error
    """
    # Buscar tarea por ID
    task = next((t for t in tasks if t["id"] == task_id), None)
    
    if not task:
        return jsonify({
            "error": "Tarea no encontrada",
            "mensaje": f"No existe una tarea con ID {task_id}"
        }), 404
    
    # Validar que el request contenga JSON
    if not request.json:
        return jsonify({
            "error": "Formato inválido",
            "mensaje": "El body debe ser JSON"
        }), 400
    
    # Actualizar campos proporcionados
    if "titulo" in request.json:
        task["titulo"] = request.json["titulo"]
    if "descripcion" in request.json:
        task["descripcion"] = request.json["descripcion"]
    if "completada" in request.json:
        task["completada"] = request.json["completada"]
    
    return jsonify({
        "mensaje": "Tarea actualizada exitosamente",
        "tarea": task
    }), 200


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Elimina una tarea
    Parámetros:
        task_id (int): ID de la tarea a eliminar
    Retorna: Confirmación de eliminación o mensaje de error
    """
    global tasks
    
    # Buscar índice de la tarea
    task_index = next((i for i, t in enumerate(tasks) if t["id"] == task_id), None)
    
    if task_index is None:
        return jsonify({
            "error": "Tarea no encontrada",
            "mensaje": f"No existe una tarea con ID {task_id}"
        }), 404
    
    # Eliminar tarea
    deleted_task = tasks.pop(task_index)
    
    return jsonify({
        "mensaje": "Tarea eliminada exitosamente",
        "tarea_eliminada": deleted_task
    }), 200


# ==================== MANEJO DE ERRORES ====================

@app.errorhandler(404)
def not_found(error):
    """Maneja rutas no encontradas"""
    return jsonify({
        "error": "Endpoint no encontrado",
        "mensaje": "La ruta solicitada no existe en esta API"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Maneja errores internos del servidor"""
    return jsonify({
        "error": "Error interno del servidor",
        "mensaje": "Ocurrió un error inesperado"
    }), 500


# ==================== EJECUCIÓN ====================

if __name__ == '__main__':
    # Ejecutar aplicación en el puerto 8000
    # host='0.0.0.0' permite acceso desde fuera del contenedor
    # debug=True proporciona información detallada de errores (solo desarrollo)
    app.run(host='0.0.0.0', port=8000, debug=True)