
import os

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS  # ✅ Import CORS

from Routes.AnswerRoutes import bertAnswer_bp
from Routes.BertRoutes import bert_bp
from Routes.PersonRoutes import person_bp
from Routes.KnowledgeBaseRoutes import knowledge_base_bp
from Routes.CategoryRoutes import category_bp
from Routes.SessionRoutes import session_bp
from Routes.ChatRoutes import chat_bp
from db import db

app = Flask(__name__)

CORS(app)

# Configure the app with the necessary SQL Server URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:123@DESKTOP-67L2GN9\\SQLEXPRESS/Chatbot?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register the blueprints
app.register_blueprint(person_bp)
# app.register_blueprint(bert_bp)
app.register_blueprint(bertAnswer_bp)
app.register_blueprint(knowledge_base_bp)
app.register_blueprint(category_bp)
# app.register_blueprint(program_bp)
app.register_blueprint(session_bp)
app.register_blueprint(chat_bp)

@app.route('/')
def welcome():
    return jsonify({'message': 'Welcome to the Chatbot API! The server is running.'})



@app.route('/modelAnswer/<filename>')
def serve_model_answer(filename):
    model_answers_dir = os.path.join(os.getcwd(), 'Uploads', 'ModelAnswers')
    return send_from_directory(
        model_answers_dir,
        filename,
        mimetype='audio/aac'  # Ensure it's served as an AAC audio file
    )

if __name__ == "__main__":
    app.run(host ="0.0.0.0",port=5000, debug=True)
