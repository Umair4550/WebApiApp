from flask import Blueprint, request, jsonify
from App.db import db
from App.Models.DbModels import Program

program_bp = Blueprint('program', __name__)

# CREATE Program
@program_bp.route('/program', methods=['POST'])
def create_program():
    data = request.get_json()
    program = Program(Name=data['Name'])
    db.session.add(program)
    db.session.commit()
    return jsonify({'message': 'Program created'}), 201

# READ Program
@program_bp.route('/program/<int:id>', methods=['GET'])
def get_program(id):
    program = Program.query.get_or_404(id)
    return jsonify({'Pid': program.Pid, 'Name': program.Name})

# UPDATE Program
@program_bp.route('/program/<int:id>', methods=['PUT'])
def update_program(id):
    program = Program.query.get_or_404(id)
    data = request.get_json()
    program.Name = data.get('Name', program.Name)
    db.session.commit()
    return jsonify({'message': 'Program updated'})

# DELETE Program
@program_bp.route('/program/<int:id>', methods=['DELETE'])
def delete_program(id):
    program = Program.query.get_or_404(id)
    db.session.delete(program)
    db.session.commit()
    return jsonify({'message': 'Program deleted'})
