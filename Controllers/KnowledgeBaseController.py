from flask import jsonify, request
from requests import session

from Models.KnowledgeBase import KnowledgeBase
from db import db
import re

class KnowledgeBaseController:

    @staticmethod
    def add_entry():
        try:
            data = request.json

            if not all(key in data for key in ['key', 'value']):
                return jsonify({'error': 'Missing required fields: Key and Value'}), 400

            new_entry = KnowledgeBase(
                key=data.get('key'),
                value=data.get('value'),

            )
            db.session.add(new_entry)
            db.session.commit()
            return jsonify({'message': 'Entry added successfully!'}), 201
        except Exception as e:
            return jsonify({'error': f"Failed to add entry: {str(e)}"}), 500

    @staticmethod
    def get_all_entries():
        try:
            entries = KnowledgeBase.query.filter_by(isDeleted=False)
            return jsonify([entry.as_dict() for entry in entries])
        except Exception as e:
            return jsonify({'error': f"Failed to fetch entries: {str(e)}"}), 500

    @staticmethod
    def get_entry_by_id(id):
        try:
            entry = KnowledgeBase.query.get(id)
            if entry:
                return jsonify(entry.as_dict())
            else:
                return jsonify({'error': 'Entry not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to fetch entry: {str(e)}"}), 500

    @staticmethod
    def update_entry(id):
        try:
            data = request.json
            # Validate that at least one field is provided to update
            if not any(key in data for key in ['key', 'value']):
                return jsonify({'error': 'No fields provided to update'}), 400

            entry = KnowledgeBase.query.get(id)
            if entry:
                entry.key = data.get('key', entry.key)
                entry.value = data.get('value', entry.value)
                db.session.commit()
                return jsonify({'message': 'Entry updated successfully!', 'entry': entry.as_dict()})
            else:
                return jsonify({'error': 'Entry not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to update entry: {str(e)}"}), 500

    @staticmethod
    def delete_entry(id):
        try:
            entry = KnowledgeBase.query.get(id)
            if entry:
                entry.isDeleted=True
                db.session.commit()
                return jsonify({'message': 'Entry deleted successfully!'})
            else:
                return jsonify({'error': 'Entry not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to delete entry: {str(e)}"}),500

    @staticmethod
    def process_answer():
        try:
            # Get the answer from the request
            data = request.get_json()
            answer = data.get('answer')
           # id=data.get("sid")

            if not answer:
                return jsonify({"error": "Answer is required"}), 400

            # Fetch the tag-value mappings from the database
            tag_values = {entry.key: entry.value for entry in KnowledgeBase.query.filter_by(isDeleted=False).all()}

            # Replace tags in the answer
            processed_answer = re.sub(r"<(.*?)>", lambda match: tag_values.get(match.group(1), match.group(0)), answer)

            return jsonify({"processed_answer": processed_answer}), 200

        except Exception as e:
            return jsonify({"error": f"Failed to process answer: {str(e)}"}), 500
