from flask import Blueprint, jsonify
from Controllers.ProgramController import ProgramController

# Create a Blueprint for Program
program_bp = Blueprint('program', __name__)

# Route to get all programs
@program_bp.route('/program', methods=['GET'])
def get_programs():
    try:
        return ProgramController.get_all_programs()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new program
@program_bp.route('/program', methods=['POST'])
def add_program():
    try:
        return ProgramController.add_program()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a program by ID
@program_bp.route('/program/<int:program_id>', methods=['GET'])
def get_program_by_id(program_id):
    try:
        return ProgramController.get_program_by_id(program_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a program by ID
@program_bp.route('/program/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    try:
        return ProgramController.update_program(program_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a program by ID
@program_bp.route('/program/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    try:
        return ProgramController.delete_program(program_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
