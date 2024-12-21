from flask import Flask, jsonify
from sympy import false

from App.db import db, create_app

app = create_app()

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask API with CRUD Operations!"), 200

if __name__ == "__main__":
    # Create the database tables if they don't exist (this can be done once when the app starts)
    # with app.app_context():
    #     db.create_all()  # Creates all tables based on models if they don't exist

    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=false)
