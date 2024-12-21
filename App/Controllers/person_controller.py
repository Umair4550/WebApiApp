from flask import Blueprint, request, jsonify
from App.db import db
from App.Models.DbModels import Person  # Assuming Person model exists in models/person.py

person_bp = Blueprint('person_controller', __name__)

# CREATE Person
@person_bp.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    try:
        person = Person(
            Name=data['Name'],
            Phno=data['Phno'],
            Password=data['Password'],
            Profile_url=data['Profile_url']
        )
        db.session.add(person)
        db.session.commit()
        return jsonify({'message': 'Person created successfully', 'Pid': person.Pid}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f"Error: {str(e)}"}), 400

# READ all persons
@person_bp.route('/person', methods=['GET'])
def get_all_persons():
    try:
        persons = Person.query.all()
        return jsonify([{
            'Pid': person.Pid,
            'Name': person.Name,
            'Phno': person.Phno,
            "Password":person.Password,
            'Profile_url': person.Profile_url,

        } for person in persons]), 200
    except Exception as e:
        return jsonify({'message': f"Error: {str(e)}"}), 500

# READ a specific person by ID
@person_bp.route('/person/<int:id>', methods=['GET'])
def get_person(id):
    try:
        person = Person.query.get_or_404(id)
        return jsonify({
            'Pid': person.Pid,
            'Name': person.Name,
            'Phno': person.Phno,
            'Profile_url': person.Profile_url
        }), 200
    except Exception as e:
        return jsonify({'message': f"Error: {str(e)}"}), 500

# UPDATE Person by ID
@person_bp.route('/person/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    try:
        person = Person.query.get_or_404(id)

        person.Name = data.get('Name', person.Name)
        person.Phno = data.get('Phno', person.Phno)
        person.Password = data.get('Password', person.Password)
        person.Profile_url = data.get('Profile_url', person.Profile_url)

        db.session.commit()
        return jsonify({'message': 'Person updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f"Error: {str(e)}"}), 400

# DELETE Person by ID
@person_bp.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    try:
        person = Person.query.get_or_404(id)
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f"Error: {str(e)}"}), 400
