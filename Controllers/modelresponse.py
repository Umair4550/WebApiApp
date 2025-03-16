import numpy as np
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv(r"", encoding='latin-1')

# Load pre-trained BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert all questions to embeddings
question_texts = df['Question'].tolist()
answer_texts = df['Answer'].tolist()
label_texts = df['Label'].tolist()

question_embeddings = model.encode(question_texts, convert_to_numpy=True)

# Store embeddings in FAISS index
dimension = question_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(question_embeddings)

# Save FAISS index and dataset for retrieval
faiss.write_index(index, "question_embeddings.index")
np.save("question_texts.npy", np.array(question_texts))
np.save("answer_texts.npy", np.array(answer_texts))
np.save("label_texts.npy", np.array(label_texts))

print("Model training completed! Saved embeddings, answers, and labels for fast retrieval.")
