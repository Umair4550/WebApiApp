from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from App.Controllers.BertController import bert_bp

# Initialize the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:1234@DESKTOP-67L2GN9\\SQLEXPRESS/FYP?driver=ODBC+Driver+17+for+SQL+Server'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # Register Blueprints for all controllers
    from App.Controllers.person_controller import person_bp
    from App.Controllers.session_controller import session_bp
    from App.Controllers.category_controller import category_bp
    from App.Controllers.program_controller import program_bp
    from App.Controllers.chat_controller import chat_bp

    app.register_blueprint(person_bp, url_prefix='/api/persons')
    app.register_blueprint(session_bp, url_prefix='/api/sessions')
    app.register_blueprint(category_bp, url_prefix='/api/categories')
    app.register_blueprint(program_bp, url_prefix='/api/programs')
    app.register_blueprint(chat_bp, url_prefix='/api/chats')
    app.register_blueprint(bert_bp, url_prefix='/api')


    return app
