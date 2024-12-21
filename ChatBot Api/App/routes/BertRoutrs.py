from flask import request, jsonify, Flask
from App.Controllers.BertController import BertController

# Initialize Flask app and BertController
app = Flask(__name__)
bert = BertController()

@app.route('/get_model_report', methods=['GET'])
def get_model_report():
    # Get the classification report and accuracy
    try:
        report = bert.get_model_report()
        return jsonify(report)
    except Exception as e:
        return jsonify({"error": f"Failed to generate model report: {str(e)}"}), 500

@app.route('/classify_query', methods=['POST'])
def classify_query():
    # Classify the provided query
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Query not provided"}), 400
    try:
        query = data['query']
        result = bert.classify_query(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Failed to classify query: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
