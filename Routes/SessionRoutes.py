from flask import Blueprint, jsonify
from Controllers.SessionController import SessionController

# Create a Blueprint for Session
session_bp = Blueprint('session', __name__)

# Route to get all sessions
@session_bp.route('/session', methods=['GET'])
def get_all_sessions():
    try:
        return SessionController.get_all_sessions()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new session
@session_bp.route('/session', methods=['POST'])
def add_session():
    try:
        return SessionController.add_session()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a session by ID
@session_bp.route('/session/<int:sid>', methods=['GET'])
def get_session_by_id(sid):
    try:
        return SessionController.get_session_by_id(sid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a session by ID
@session_bp.route('/session/<int:sid>', methods=['PUT'])
def update_session(sid):
    try:
        return SessionController.update_session(sid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a session by ID
@session_bp.route('/session/<int:sid>', methods=['DELETE'])
def delete_session(sid):
    try:
        return SessionController.delete_session(sid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
