from flask import Blueprint, request, jsonify
from Controllers.PersonController import PersonController


person_bp = Blueprint('person', __name__)
# Get all people
@person_bp.route('/person', methods=['GET'])
def get_people():
    try:
        return PersonController.get_person()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Create a new person
@person_bp.route('/person', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Assuming PersonController has a method to create a person
        return PersonController.add_person(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get person by ID
@person_bp.route('/person/<int:person_id>', methods=['GET'])
def get_person_by_id(person_id):
    try:
        return PersonController.get_person_by_id(person_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@person_bp.route('/person/login', methods=['POST'])
def login():
    try:
        return PersonController.login_user()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update person by ID
@person_bp.route('/person/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        return PersonController.update_person(person_id, data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete person by ID
@person_bp.route('/person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    try:
        return PersonController.delete_person(person_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
