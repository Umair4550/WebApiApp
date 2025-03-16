from flask import Blueprint, jsonify
from Controllers.KnowledgeBaseController import KnowledgeBaseController

# Create a Blueprint for KnowledgeBase
knowledge_base_bp = Blueprint('knowledge_base', __name__)

# Route to get all knowledge base entries
@knowledge_base_bp.route('/knowledgeBase', methods=['GET'])
def get_all_entries():
    try:
        return KnowledgeBaseController.get_all_entries()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new knowledge base entry
@knowledge_base_bp.route('/knowledgeBase', methods=['POST'])
def add_entry():
    try:
        return KnowledgeBaseController.add_entry()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a knowledge base entry by ID
@knowledge_base_bp.route('/knowledgeBase/<int:kbid>', methods=['GET'])
def get_entry_by_id(kbid):
    try:
        return KnowledgeBaseController.get_entry_by_id(kbid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a knowledge base entry by ID
@knowledge_base_bp.route('/knowledgeBase/<int:kbid>', methods=['PUT'])
def update_entry(kbid):
    try:
        return KnowledgeBaseController.update_entry(kbid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a knowledge base entry by ID
@knowledge_base_bp.route('/knowledgeBase/<int:kbid>', methods=['DELETE'])
def delete_entry(kbid):
    try:
        return KnowledgeBaseController.delete_entry(kbid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@knowledge_base_bp.route('/process_answer', methods=['GET'])
def process_answer():
    try:
        return KnowledgeBaseController.process_answer()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
