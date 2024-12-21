from flask import Blueprint, request, jsonify
from App.db import db
from App.Models.DbModels import Category

category_bp = Blueprint('category', __name__)

# CREATE Category
@category_bp.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()
    category = Category(Title=data['Title'])
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created'}), 201

# READ Category
@category_bp.route('/category/<int:id>', methods=['GET'])
def get_category(id):
    category = Category.query.get_or_404(id)
    return jsonify({'Cid': category.Cid, 'Title': category.Title})

# UPDATE Category
@category_bp.route('/category/<int:id>', methods=['PUT'])
def update_category(id):
    category = Category.query.get_or_404(id)
    data = request.get_json()
    category.Title = data.get('Title', category.Title)
    db.session.commit()
    return jsonify({'message': 'Category updated'})

# DELETE Category
@category_bp.route('/category/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted'})
