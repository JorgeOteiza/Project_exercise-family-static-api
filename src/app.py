"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructures import FamilyStructure
from utils import APIException, generate_sitemap

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Inicializar la familia Jackson
jackson_family = FamilyStructure('Jackson')

# Endpoint para obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para obtener un miembro específico
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"error": "Miembro no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para agregar un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    try:
        member_data = request.get_json()
        if not member_data:
            return jsonify({"error": "Datos de entrada no proporcionados"}), 400

        # Validar campos obligatorios
        required_fields = ["first_name", "age", "lucky_numbers"]
        for field in required_fields:
            if field not in member_data:
                return jsonify({"error": f"El campo '{field}' es obligatorio"}), 400

        jackson_family.add_member(member_data)
        return jsonify({"message": "Miembro agregado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para eliminar un miembro
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member:
            jackson_family.delete_member(member_id)
            return jsonify({"done": True}), 200
        else:
            return jsonify({"error": "Miembro no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Manejo de errores
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generar sitemap
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
