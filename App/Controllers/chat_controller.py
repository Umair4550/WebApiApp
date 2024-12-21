from flask import Blueprint, request, jsonify
from App.db import db
from App.Models.DbModels import Chat

chat_bp = Blueprint('chat', __name__)

# CREATE Chat
@chat_bp.route('/chat', methods=['POST'])
def create_chat():
    data = request.get_json()
    chat = Chat(
        Question=data['Question'],
        Answer=data['Answer'],
        Date=data['Date'],
        Time=data['Time'],
        Pid=data['Pid'],
        Sid=data['Sid'],
        CategoryId=data['CategoryId'],
        Program_Id=data['Program_Id']
    )
    db.session.add(chat)
    db.session.commit()
    return jsonify({'message': 'Chat created'}), 201

# READ Chat
@chat_bp.route('/chat/<int:id>', methods=['GET'])
def get_chat(id):
    try:
        chat = Chat.query.get_or_404(id)
        return jsonify({
            'Id': chat.Id,
            'Question': chat.Question,
            'Answer': chat.Answer,
            'Date': chat.Date,
            'Time': chat.Time,
            'Pid': chat.Pid,
            'Sid': chat.Sid,
            'CategoryId': chat.CategoryId,
            'Program_Id': chat.Program_Id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# UPDATE Chat
@chat_bp.route('/chat/<int:id>', methods=['PUT'])
def update_chat(id):
    chat = Chat.query.get_or_404(id)
    data = request.get_json()
    chat.Question = data.get('Question', chat.Question)
    chat.Answer = data.get('Answer', chat.Answer)
    chat.Date = data.get('Date', chat.Date)
    chat.Time = data.get('Time', chat.Time)
    chat.Pid = data.get('Pid', chat.Pid)
    chat.Sid = data.get('Sid', chat.Sid)
    chat.CategoryId = data.get('CategoryId', chat.CategoryId)
    chat.Program_Id = data.get('Program_Id', chat.Program_Id)
    db.session.commit()
    return jsonify({'message': 'Chat updated'})

# DELETE Chat
@chat_bp.route('/chat/<int:id>', methods=['DELETE'])
def delete_chat(id):
    chat = Chat.query.get_or_404(id)
    db.session.delete(chat)
    db.session.commit()
    return jsonify({'message': 'Chat deleted'})


# Get all Chats by User ID (Pid)
@chat_bp.route('/chats/program/<int:prid>', methods=['GET'])
def get_chats_by_program_id(prid):
    # Fetch all chats for the given Pid (User ID)
    chats = Chat.query.filter_by(Program_Id=prid).all()

    # Check if there are no chats
    if not chats:
        return jsonify({'message': 'No chats found for this user.'}), 404

    # Format the chat data and return
    chat_list = [
        {
            'Id': chat.Id,
            'Question': chat.Question,
            'Answer': chat.Answer,
            'Date': chat.Date,
            'Time': chat.Time,
            'Pid': chat.Pid,
            'Sid': chat.Sid,
            'CategoryId': chat.CategoryId,
            'Program_Id': chat.Program_Id
        }
        for chat in chats
    ]
    return jsonify({'chats': chat_list})


# Alternatively, if you need to get by Sid (Session ID)
@chat_bp.route('/chats/session/<int:sid>', methods=['GET'])
def get_chats_by_sid(sid):
    # Fetch all chats for the given Sid (Session ID)
    chats = Chat.query.filter_by(Sid=sid).all()

    # Check if there are no chats
    if not chats:
        return jsonify({'message': 'No chats found for this session.'}), 404

    # Format the chat data and return
    chat_list = [
        {
            'Id': chat.Id,
            'Question': chat.Question,
            'Answer': chat.Answer,
            'Date': chat.Date,
            'Time': chat.Time,
            'Pid': chat.Pid,
            'Sid': chat.Sid,
            'CategoryId': chat.CategoryId,
            'Program_Id': chat.Program_Id
        }
        for chat in chats
    ]
    return jsonify({'chats': chat_list})
# Get all Chats by Program ID
@chat_bp.route('/chats/user/<int:pid>', methods=['GET'])
def get_chats_by_pid(pid):
    try:
        chats = Chat.query.filter_by(Pid=pid).all()

        if not chats:
            return jsonify({'message': 'No chats found for this user.'}), 404

        chat_list = [
            {
                'Id': chat.Id,
                'Question': chat.Question,
                'Answer': chat.Answer,
                'Date': chat.Date,
                'Time': chat.Time,
                'Pid': chat.Pid,
                'Sid': chat.Sid,
                'CategoryId': chat.CategoryId,
                'Program_Id': chat.Program_Id
            }
            for chat in chats
        ]
        return jsonify({'chats': chat_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# DELETE Chats by User ID (Pid)
@chat_bp.route('/chats/user/<int:pid>', methods=['DELETE'])
def delete_chats_by_pid(pid):
    try:
        chats = Chat.query.filter_by(Pid=pid).all()

        if not chats:
            return jsonify({'message': 'No chats found for this user to delete.'}), 404

        for chat in chats:
            db.session.delete(chat)
        db.session.commit()

        return jsonify({'message': f'All chats for user with Pid {pid} have been deleted.'})
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500


# Route to get all chats
@chat_bp.route('/chat', methods=['GET'])
def get_all_chats():
    try:
        # Fetch all chat records from the database
        chats = Chat.query.all()

        # If no chats exist, return a message
        if not chats:
            return jsonify({'message': 'No chats found'}), 404

        # Format the chat data into a list of dictionaries
        chat_list = [
            {
                'Id': chat.Id,
                'Question': chat.Question,
                'Answer': chat.Answer,
                'Date': chat.Date,
                'Time': chat.Time,
                'Pid': chat.Pid,
                'Sid': chat.Sid,
                'CategoryId': chat.CategoryId,
                'Program_Id': chat.Program_Id
            }
            for chat in chats
        ]

        # Return the list of chats as JSON
        return jsonify({'chats': chat_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
