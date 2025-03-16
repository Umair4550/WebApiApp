from flask import Blueprint, jsonify, request
from Controllers.BertController import BertController

# Create a Blueprint for BERT-related routes
bert_bp = Blueprint('bert', __name__)

# Instantiate the BertController
bert_controller = BertController()

@bert_bp.route('/get_model_report', methods=['GET'])
def get_model_report():
    """
    Get the classification report and accuracy.
    """
    try:
        report = bert_controller.get_model_report()
        return jsonify({"success": True, "data": report}), 200
    except Exception as e:
        return jsonify({"success": False, "error": f"Failed to generate model report: {str(e)}"}), 500

@bert_bp.route('/classify_query', methods=['POST'])
def classify_query():
    """
    Classify the provided query.
    """
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"success": False, "error": "Query not provided"}), 400
    try:
        query = data['query']
        result = bert_controller.classify_query(query)
        return jsonify({"success": True, "data": result}), 200
    except Exception as e:
        return jsonify({"success": False, "error": f"Failed to classify query: {str(e)}"}), 500
