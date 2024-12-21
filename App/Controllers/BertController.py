from flask import Blueprint, request, jsonify
from App.Models.BertModel import BertModel  # Assuming BertModel is saved in 'App/Models/BertModel.py'

bert_bp = Blueprint('bert', __name__)

controller = BertModel()


# Route to get the model's performance report (accuracy)
@bert_bp.route('/get_report', methods=['GET'])
def get_report():
    """
    Route to get the model's accuracy and performance report.
    """
    try:
        report = controller.get_model_report()
        return jsonify(report)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bert_bp.route('/classify_query', methods=['GET'])
def classify_query():
    """
    Route to classify a given query.
    Expects the query as a URL parameter (GET request).
    """
    try:
        query = request.args.get('query')

        if not query:
            return jsonify({"error": "No query provided"}), 400

        # Get the classification result from the BertModel controller
        result = controller.classify_query(query)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500