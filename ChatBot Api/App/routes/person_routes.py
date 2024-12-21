# routes/person_routes.py
from flask import Blueprint, request, jsonify
from controllers.person_controller import create_person, get_person, update_person, delete_person

person_bp = Blueprint('person', __name__)

@person_bp.route('/person', methods=['POST'])
def add_person():
    data = request.get_json()
    person = create_person(data['name'], data['phno'], data['password'], data['profile_url'])
    return jsonify({'id': person.Pid, 'name': person.Name}), 201

@person_bp.route('/person/<int:pid>', methods=['GET'])
def get_person_route(pid):
    person = get_person(pid)
    return jsonify({'id': person.Pid, 'name': person.Name, 'phno': person.Phno})

@person_bp.route('/person/<int:pid>', methods=['PUT'])
def update_person_route(pid):
    data = request.get_json()
    person = update_person(pid, data.get('name'), data.get('phno'), data.get('password'), data.get('profile_url'))
    return jsonify({'id': person.Pid, 'name': person.Name})

@person_bp.route('/person/<int:pid>', methods=['DELETE'])
def delete_person_route(pid):
    person = delete_person(pid)
    return jsonify({'message': f'Person {person.Name} deleted'}), 200
