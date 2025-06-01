from flask import jsonify, request
from requests import session

from Models.Session import Session
from db import db

class SessionController:

    @staticmethod
    def add_session():
        try:
            data = request.json
            if not data or not data.get('title'):
                return jsonify({'error': 'title is required'}), 400

            new_session = Session(
                title=data.get('title')
            )
            db.session.add(new_session)
            db.session.commit()
            return jsonify({'message': 'Session added successfully!', 'session': new_session.as_dict()}), 201
        except Exception as e:
            return jsonify({'error': f"Failed to add session: {str(e)}"}), 500

    @staticmethod
    def get_all_sessions():
        try:
            sessions = Session.query.filter_by(isDeleted=False).all()
            return jsonify([session.as_dict() for session in sessions])
        except Exception as e:
            return jsonify({'error': f"Failed to fetch sessions: {str(e)}"}), 500

    @staticmethod
    def get_current_session():
        try:
            # Get the last added session (assuming higher 'id' means newer)
            #session = Session.query.filter_by(isDeleted=False).order_by(Session.id.desc()).first()
            currentSession=Session.query.filter_by(isActive=True).first()

            if currentSession:
                return jsonify(currentSession.as_dict())
            else:
                return jsonify({'message': 'No active session found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to fetch current session: {str(e)}"}), 500

    @staticmethod
    def set_active_session(session_id):
        try:
            # Set all sessions to inactive first
            Session.query.update({Session.isActive: False})
            db.session.commit()

            # Activate the selected session
            session = Session.query.get(session_id)
            if session:
                session.isActive = True
                db.session.commit()
                return jsonify({'message': 'Session activated successfully'}), 200
            else:
                return jsonify({'error': 'Session not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_session_by_id(sid):
        try:
            session = Session.query.filter_by(id=sid, isDeleted=False).first()
            if session:
                return jsonify(session.as_dict())
            else:
                return jsonify({'error': 'Session not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to fetch session: {str(e)}"}), 500

    @staticmethod
    def update_session(sid):
        try:
            data = request.json
            session = Session.query.filter_by(id=sid, isDeleted=False).first()
            if session:
                session.title = data.get('title', session.title)
                db.session.commit()
                return jsonify({'message': 'Session updated successfully!', 'session id': session.id})
            else:
                return jsonify({'error': 'Session not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to update session: {str(e)}"}), 500

    @staticmethod
    def delete_session(sid):
        try:
            session = Session.query.filter_by(id=sid, isDeleted=False).first()
            if session:
                session.isDeleted = True
                db.session.commit()
                return jsonify({'message': 'Session deleted successfully!'})
            else:
                return jsonify({'error': 'Session not found'}), 404
        except Exception as e:
            return jsonify({'error': f"Failed to delete session: {str(e)}"}), 500
