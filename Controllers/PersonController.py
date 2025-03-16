from flask import jsonify, request
from Models.Person import Person
from db import db  # Import the db object from db.py

class PersonController:

    @staticmethod
    def add_person(data):
        try:
            # Validate required fields
            if not all(key in data for key in ['Name', 'Phno', 'Password', 'Profile_Url']):
                return jsonify({'error': 'Missing required fields'}), 400

            new_person = Person(
                Name=data['Name'],
                Phno=data['Phno'],
                Password=data['Password'],
                Profile_Url=data['Profile_Url']
            )
            db.session.add(new_person)  # Add the person to the session
            db.session.commit()  # Commit the transaction to the database
            return jsonify({'message': 'Person added successfully!', 'person_id:': new_person.id}), 201
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
            if not any(key in data for key in ['Name', 'Phno', 'Password', 'Profile_Url']):
                return jsonify({'error': 'No fields provided to update'}), 400

            person = Person.query.filter_by(id=person_id, isDeleted=False).first()
            if person:
                # Dynamically update fields that are provided in the request
                if 'Name' in data:
                    person.Name = data['Name']
                if 'Phno' in data:
                    person.phno = data['Phno']
                if 'Password' in data:
                    person.Password = data['Password']
                if 'Profile_Url' in data:
                    person.Profile_Url = data['Profile_Url']

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
