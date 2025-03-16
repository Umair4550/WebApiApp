from flask import jsonify, request
from Models.Program import Program
from db import db  # Import the db object from db.py

class ProgramController:

    @staticmethod
    def add_program():
        try:
            data = request.json
            if not data or not data.get('name'):
                return jsonify({'error': 'name is required'}), 400

            new_program = Program(name=data['name'])
            db.session.add(new_program)
            db.session.commit()
            return jsonify({'message': 'Program added successfully!', 'id': new_program.id}), 201
        except Exception as e:
            return jsonify({'error': f"Failed to add program: {str(e)}"}), 500

    @staticmethod
    def get_program_by_id(program_id):
        try:
            program = Program.query.filter_by(id=program_id, isDeleted=False).first()  # Changed Pr_id to id
            if program:
                return jsonify(program.as_dict())
            else:
                return jsonify({'error': 'Program not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to fetch program: {str(e)}"}), 500

    @staticmethod
    def update_program(program_id):
        try:
            data = request.json
            program = Program.query.filter_by(id=program_id, isDeleted=False).first()  # Changed Pr_id to id
            if program:
                program.name = data.get('name', program.name)  # Changed Pname to name
                db.session.commit()
                return jsonify({'message': 'Program updated successfully!', 'program': program.as_dict()})
            else:
                return jsonify({'error': 'Program not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to update program: {str(e)}"}), 500

    @staticmethod
    def delete_program(program_id):
        try:
            program = Program.query.filter_by(id=program_id, isDeleted=False).first()  # Changed Pr_id to id
            if program:
                program.isDeleted = True
                db.session.commit()
                return jsonify({'message': 'Program deleted successfully!'})
            else:
                return jsonify({'error': 'Program not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to delete program: {str(e)}"}), 500

    @staticmethod
    def get_all_programs():
        try:
            programs = Program.query.filter_by(isDeleted=False).all()
            return jsonify([program.as_dict() for program in programs])
        except Exception as e:
            return jsonify({'error': f"Failed to fetch programs: {str(e)}"}), 500
