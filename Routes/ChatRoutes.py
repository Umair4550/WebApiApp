from flask import Blueprint, jsonify
from Controllers.ChatController import ChatController

# Create a Blueprint for Chat
chat_bp = Blueprint('chat', __name__)

# Route to get all chats
@chat_bp.route('/chat', methods=['GET'])
def get_all_chats():
    try:
        return ChatController.get_all_chats()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new chat
@chat_bp.route('/chat', methods=['POST'])
def add_chat():
    try:
        return ChatController.add_chat()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a chat by ID
@chat_bp.route('/chat/<int:cid>', methods=['GET'])
def get_chat_by_id(cid):
    try:
        return ChatController.get_chat_by_id(cid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a chat by ID
@chat_bp.route('/chat/<int:cid>', methods=['PUT'])
def update_chat(cid):
    try:
        return ChatController.update_chat(cid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/chat/<int:cid>', methods=['DELETE'])
def delete_chat(cid):
    try:
        return ChatController.delete_chat(cid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to get chats by person ID
@chat_bp.route('/chat/person/<int:person_id>', methods=['GET'])
def get_chats_by_person(person_id):
    try:
        return ChatController.get_chats_by_person(person_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to count chats by person ID
@chat_bp.route('/chat/person/<int:person_id>/count', methods=['GET'])
def count_chats_by_person(person_id):
    try:
        return ChatController.count_chats_by_person(person_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to count chats by program ID
@chat_bp.route('/chat/program/<int:program_id>/count', methods=['GET'])
def count_chats_by_program(program_id):
    try:
        return ChatController.count_chats_by_program(program_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to count chats by session ID
@chat_bp.route('/chat/session/<int:session_id>/count', methods=['GET'])
def count_chats_by_session(session_id):
    try:
        return ChatController.count_chats_by_session(session_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to count chats by category ID
@chat_bp.route('/chat/category/<int:category_id>/count', methods=['GET'])
def count_chats_by_category(category_id):
    try:
        return ChatController.count_chats_by_category(category_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get total chats by session title
@chat_bp.route('/chat/session/title/<string:session_title>', methods=['GET'])
def get_total_chats_by_session_title(session_title):
    try:
        return ChatController.count_chats_by_session_title(session_title)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get chats of all persons by session title
@chat_bp.route('/chat/session/title/<string:session_title>', methods=['GET'])
def get_chats_of_all_persons_by_session_title(session_title):
    try:
        return ChatController.get_chats_of_all_persons_by_session_title(session_title)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Route to get total chats by category title
@chat_bp.route('/chat/categoryReport', methods=['GET'])
def get_total_chats_by_category_title():
    try:
        return ChatController.categoryreport()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get total chats by category title for a specific program
# @chat_bp.route('/chat/categoryReport/<string:program_title>', methods=['GET'])
# def get_total_chats_by_category_title_for_program(program_title):
#     try:
#         return ChatController.categoryreportbyprogram(program_title)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# Route to get total chats by session title across all categories
@chat_bp.route('/chat/sessionReport', methods=['GET'])
def get_total_chats_by_session_title_across_all_categories():
    try:
        return ChatController.sessionreport()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# # Route to get total chats by session title for a specific program
# @chat_bp.route('/chat/sessionReport/<string:program_title>', methods=['GET'])
# def get_total_chats_by_session_title_for_program(program_title):
#     try:
#         return ChatController.sessionreportbyprogram(program_title)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# Route to get chat summary
@chat_bp.route('/chat/summary', methods=['GET'])
def get_chat_summary():
    try:
        return ChatController.get_chat_summary()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get chats by date range
@chat_bp.route('/chat/DateRange/<start_date>/<end_date>', methods=['GET'])
def get_chats_by_date_range(start_date, end_date):
    try:
        return ChatController.get_chats_by_date_range(start_date, end_date)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@chat_bp.route('/chat/categoryReport/<int:sid>', methods=['GET'])
def get_categoryReport_sid(sid):
    try:
        return ChatController.category_report_by_session(sid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
