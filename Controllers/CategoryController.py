from flask import jsonify, request
from Models.Category import Category
from db import db

class CategoryController:

    @staticmethod
    def add_category():
        try:
            data = request.json
            if not data.get('title'):
                return jsonify({'error': 'title is required'}), 400

            new_category = Category(
                title=data.get('title')
            )
            db.session.add(new_category)
            db.session.commit()
            return jsonify({'message': 'Category added successfully!'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_all_categories():
        try:
            categories = Category.query.all()
            return jsonify([category.as_dict() for category in categories])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_category_by_id(id):
        try:
            category = Category.query.get_or_404(id)
            return jsonify(category.as_dict())
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def update_category(id):
        try:
            data = request.json
            if not data.get('title'):
                return jsonify({'error': 'title is required'}), 400

            category = Category.query.get(id)
            if category:
                category.title = data.get('title', category.title)
                db.session.commit()
                return jsonify({'message': 'Category updated successfully!', 'category': category.as_dict()})
            return jsonify({'error': 'Category not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def delete_category(cid):
        try:
            category = Category.query.get(cid)
            if category:
                category.isDeleted=True
                db.session.commit()
                return jsonify({'message': 'Category deleted successfully!'})
            return jsonify({'error': 'Category not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
