from flask import Blueprint, jsonify
from Controllers.CategoryController import CategoryController

# Create a Blueprint for Category
category_bp = Blueprint('category', __name__)

@category_bp.route('/category', methods=['GET'])
def get_all_categories():
    try:
        return CategoryController.get_all_categories()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@category_bp.route('/category', methods=['POST'])
def add_category():
    try:
        return CategoryController.add_category()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@category_bp.route('/category/<int:cid>', methods=['GET'])
def get_category_by_id(cid):
    try:
        return CategoryController.get_category_by_id(cid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@category_bp.route('/category/<int:cid>', methods=['PUT'])
def update_category(cid):
    try:
        return CategoryController.update_category(cid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@category_bp.route('/category/<int:cid>', methods=['DELETE'])
def delete_category(cid):
    try:
        return CategoryController.delete_category(cid)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
