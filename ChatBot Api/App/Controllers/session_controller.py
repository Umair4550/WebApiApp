from flask import Blueprint, request, jsonify
from App.db import db
from App.Models.DbModels import Session

session_bp = Blueprint('session', __name__)

# CREATE Session
@session_bp.route('/session', methods=['POST'])
def create_session():
    data = request.get_json()
    session = Session(Title=data['Title'])
    db.session.add(session)
    db.session.commit()
    return jsonify({'message': 'Session created'}), 201

# READ Session
@session_bp.route('/session/<int:id>', methods=['GET'])
def get_session(id):
    session = Session.query.get_or_404(id)
    return jsonify({'Sid': session.Sid, 'Title': session.Title})

# UPDATE Session
@session_bp.route('/session/<int:id>', methods=['PUT'])
def update_session(id):
    session = Session.query.get_or_404(id)
    data = request.get_json()
    session.Title = data.get('Title', session.Title)
    db.session.commit()
    return jsonify({'message': 'Session updated'})

# DELETE Session
@session_bp.route('/session/<int:id>', methods=['DELETE'])
def delete_session(id):
    session = Session.query.get_or_404(id)
    db.session.delete(session)
    db.session.commit()
    return jsonify({'message': 'Session deleted'})
