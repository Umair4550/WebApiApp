from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load the GPT-2 model for text generation
generator = pipeline("text-generation", model="gpt2")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    try:
        # Get the user's question from the JSON payload
        data = request.json
        query = data.get("question")

        # Validate the input
        if not query:
            return jsonify({"error": "Question is required!"}), 400

        # Generate an answer using GPT-2
        response = generator(query, max_length=100, num_return_sequences=1)
        generated_answer = response[0]['generated_text']

        # Return the response
        return jsonify({
            "query": query,
            "answer": generated_answer
        })

    except Exception as e:
        # Handle any errors
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)