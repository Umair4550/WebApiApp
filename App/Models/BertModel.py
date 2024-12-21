import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import os


class BertModel:
    def __init__(self):
        # Construct the dataset path
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Path to the current file
        dataset_path = os.path.join(base_dir, "../../Dataset/categoriesData.csv")

        # Load the dataset
        self.data = pd.read_csv(dataset_path, usecols=["Questions", "Label"])
        self.data.dropna(inplace=True)  # Drop rows with missing values

        # Label encoding for categorical labels (Admissions, Course, Irrelevant)
        self.label_encoder = LabelEncoder()
        self.data['Label'] = self.label_encoder.fit_transform(self.data['Label'])

        # Load the pre-trained Sentence-BERT model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        # Convert the 'Questions' column to embeddings
        self.sentences = self.data['Questions'].tolist()
        self.embeddings = self.model.encode(self.sentences)

        # Split data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.embeddings,
            self.data['Label'],
            test_size=0.2,
            random_state=42
        )

        # Train the Logistic Regression classifier
        self.classifier = LogisticRegression(max_iter=1000)
        self.classifier.fit(self.X_train, self.y_train)

    def get_model_report(self):
        # Evaluate the model
        y_pred = self.classifier.predict(self.X_test)
        report = classification_report(
            self.y_test,
            y_pred,
            target_names=self.label_encoder.classes_,
            output_dict=True
        )

        # Calculate accuracy
        accuracy = accuracy_score(self.y_test, y_pred)
        return {
            #"classification_report": report,
            "accuracy": f"{accuracy * 100:.2f}%"
        }

    def classify_query(self, query):
        # Encode the query into embeddings
        query_embedding = self.model.encode([query])
        prediction = self.classifier.predict(query_embedding)
        label = self.label_encoder.inverse_transform(prediction)[0]

        # Get prediction probabilities
        prediction_prob = self.classifier.predict_proba(query_embedding)

        # Classify as "Irrelevant" if confidence is low
        if max(prediction_prob[0]) < 0.6:
            label = 'Irrelevant'
        return {
            "query": query,
            "Category": label,

        }
