from flask import Blueprint, request, jsonify
import re
import pyodbc

from db import db

# Define a Blueprint for the API routes
api_blueprint = Blueprint('api', __name__)


# Fetch key-value pairs from the database
def fetch_knowledge_base():


    query = "SELECT [Key], [Value] FROM [dbo].[KnowledgeBase] WHERE [isDeleted] = 0"
    data= db.session.execute(query)

    return {row.Key: row.Value for row in data}


# Action to process the answer
@api_blueprint.route('/process_answer', methods=['POST'])
def process_answer():
    try:
        # Get the answer from the request
        data = request.get_json()
        answer = data.get('answer')

        if not answer:
            return jsonify({"error": "Answer is required"}), 400

        # Fetch the tag-value mappings from the database
        tag_values = fetch_knowledge_base()

        # Replace tags in the answer
        processed_answer = re.sub(r"<(.*?)>", lambda match: tag_values.get(match.group(1), match.group(0)), answer)

        return jsonify({"processed_answer": processed_answer}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
print(fetch_knowledge_base())