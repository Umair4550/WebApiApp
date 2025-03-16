# import numpy as np
# import pandas as pd
# import faiss
# from sentence_transformers import SentenceTransformer
#
# # Load dataset
# df = pd.read_csv(r"C:\Users\hp\PycharmProjects\ChatBot Api\Dataset\final question and answer v1.csv", encoding='latin-1')
#
# # Load pre-trained BERT model
# model = SentenceTransformer('all-MiniLM-L6-v2')
#
# # Convert all questions to embeddings
# question_texts = df['Question'].tolist()
# answer_texts = df['Answer'].tolist()
# label_texts = df['Label'].tolist()
#
# question_embeddings = model.encode(question_texts, convert_to_numpy=True)
#
# # Store embeddings in FAISS index
# dimension = question_embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(question_embeddings)
#
# # Save FAISS index and dataset for retrieval
# faiss.write_index(index, "question_embeddings.index")
# np.save("question_texts.npy", np.array(question_texts))
# np.save("answer_texts.npy", np.array(answer_texts))
# np.save("label_texts.npy", np.array(label_texts))
#
# print("Model training completed! Saved embeddings, answers, and labels for fast retrieval.")

from flask import Flask, request, jsonify
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\hp\PycharmProjects\ChatBot Api\Dataset\final question and answer v1.csv")  # Update with actual file path

# Load the pre-trained BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load stored FAISS index and question texts
index = faiss.read_index(r"C:\Users\hp\PycharmProjects\ChatBot Api\Models\ModelEmbedding\question_embeddings.index")
question_texts = np.load(r"C:\Users\hp\PycharmProjects\ChatBot Api\Models\ModelEmbedding\question_texts.npy", allow_pickle=True)

# Initialize Flask app
app = Flask(__name__)

@app.route("/get_answer", methods=["POST"])
def get_answer():
    try:
        data = request.json
        query = data.get("question")

        if not query:
            return jsonify({"error": "Question is required!"}), 400

        # Convert query into an embedding
        query_embedding = model.encode([query], convert_to_numpy=True)

        # Search for the most similar question
        _, indices = index.search(query_embedding, k=1)
        best_match = question_texts[indices[0][0]]

        # Retrieve corresponding answer
        answer_row = df[df['Question'] == best_match]

        if answer_row.empty:
            return jsonify({
                "query": query,
                "best_matched_question": best_match,
                "answer": "No answer found in the dataset."
            })

        answer = answer_row['Answer'].values[0]

        return jsonify({
            "query": query,
            "best_matched_question": best_match,
            "answer": answer
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
