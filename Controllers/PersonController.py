from flask import jsonify, request
from Models.Person import Person
from db import db  # Import the db object from db.py

class PersonController:

    @staticmethod
    def add_person(data):
        try:
            # Validate required fields
            if not all(key in data for key in ['name', 'phno', 'password']):
                return jsonify({'error': 'Missing required fields'}), 400

            new_person = Person(
                Name=data['name'],
                Phno=data['phno'],
                Password=data['password'],

            )
            db.session.add(new_person)  # Add the person to the session
            db.session.commit()  # Commit the transaction to the database
            return jsonify({'message': 'Person added successfully!', 'id': new_person.id}), 201
        except Exception as e:
            db.session.rollback()  # Rollback the session in case of error
            return jsonify({'error': f"Failed to add person: {str(e)}"}), 500

    @staticmethod
    def get_person():
        try:

            people = Person.query.filter_by(isDeleted=False).all()
            return jsonify([person.as_dict() for person in people])
        except Exception as e:
            return jsonify({'error': f"Failed to fetch people: {str(e)}"}), 500

    @staticmethod
    def get_person_by_id(person_id):
        try:
            # Query a person where isDeleted = False
            person = Person.query.filter_by(id=person_id, isDeleted=False).first()
            if person:
                return jsonify(person.as_dict())
            else:
                return jsonify({'error': 'Person not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to fetch person: {str(e)}"}), 500

    @staticmethod
    def update_person(person_id, data):
        try:
            # Validate required fields if updating
            if not any(key in data for key in ['name', 'phno', 'password', 'profile_Url']):
                return jsonify({'error': 'No fields provided to update'}), 400

            person = Person.query.filter_by(id=person_id, isDeleted=False).first()
            if person:
                # Dynamically update fields that are provided in the request
                if 'name' in data:
                    person.Name = data['Name']
                if 'phno' in data:
                    person.phno = data['phno']
                if 'password' in data:
                    person.Password = data['password']
                if 'profile_Url' in data:
                    person.Profile_Url = data['profile_Url']

                db.session.commit()  # Commit changes
                return jsonify({'message': 'Person updated successfully!'})
            else:
                return jsonify({'error': 'Person not found'}),
        except Exception as e:
            db.session.rollback()  # Rollback the session in case of error
            return jsonify({'error': f"Failed to update person: {str(e)}"}),

    @staticmethod
    def delete_person(person_id):
        try:
            person = Person.query.filter_by(id=person_id, isDeleted=False).first()
            if person:
                person.isDeleted = True
                db.session.commit()
                return jsonify({'message': 'Person deleted successfully!'})
            else:
                return jsonify({'error': 'Person not found'}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': f"Failed to delete person: {str(e)}"}), 500

    @staticmethod
    def login_user():
        try:
            data = request.get_json()
            phone_number = data.get("phno")  # Using Phno as username
            password = data.get("password")  # Password from request

            if not phone_number or not password:
                return jsonify({'error': 'Phone number and password are required'}), 400

            # Find user where isDeleted = False
            person = Person.query.filter_by(Phno=phone_number, isDeleted=False).first()

            if person:
                # Check password (If passwords are stored in plain text)
                if person.Password == password:  # Use this if passwords are NOT hashed
                    return jsonify(person.as_dict()), 200
                else:
                    return jsonify({'error': 'Invalid credentials'}), 401
            else:
                return jsonify({'error': 'User not found'}), 404

        except Exception as e:
            return jsonify({'error': f"Login failed: {str(e)}"}), 500