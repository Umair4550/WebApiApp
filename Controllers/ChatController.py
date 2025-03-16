from flask import jsonify, request
from sympy import false

from Models.Category import Category
from Models.Chat import Chat
from Models.Program import Program
from Models.Session import Session
from db import db
from sqlalchemy import func
from datetime import datetime

class ChatController:
    @staticmethod
    def get_all_chats():
        try:

            chats = Chat.query.filter_by(isDeleted=False).all()
            return jsonify([chat.as_dict() for chat in chats])
        except Exception as e:
          return jsonify({'error': f"Failed to fetch people: {str(e)}"}), 500

    @staticmethod
    def get_chat_by_id(cid):
        try:

            # Fetch the chat by ID
            chat = Chat.query.filter_by(isDeleted=False,id=cid).first()
            if chat:
                return jsonify(chat.as_dict())
            else:
                return jsonify({'error': 'Chat not found'}), 404
        except Exception as e:
            # Log the exception
            print(f"Error in get_chat_by_id: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def add_chat():
        try:
            data = request.json

            time_str = data.get('Time')
            parsed_time = datetime.strptime(time_str, "%H:%M:%S").time() if time_str else None

            new_chat = Chat(
                Question=data.get('Question'),
                Answer=data.get('Answer'),
                Time=parsed_time,
                Date=data.get('Date'),
                Person_Id=data.get('Person_Id'),
                Session_Id=data.get('Session_Id'),
                Program_Id=data.get('Program_Id'),
                Category_id=data.get('Category_id')
            )
            db.session.add(new_chat)
            db.session.commit()
            return jsonify({'message': 'Chat added successfully!', 'chat': new_chat.id}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def update_chat(cid):
        try:
            data = request.json
            chat = Chat.query.get(cid)
            if chat:
                # Parse the Time field
                time_str = data.get('Time')
                parsed_time = datetime.strptime(time_str, "%H:%M:%S").time() if time_str else chat.Time

                chat.Question = data.get('Question', chat.Question)
                chat.Answer = data.get('Answer', chat.Answer)
                chat.Time = parsed_time
                chat.Date = data.get('Date', chat.Date)
                chat.Person_Id = data.get('Person_Id', chat.Person_Id)
                chat.Session_Id = data.get('Session_Id', chat.Session_Id)
                chat.Program_Id = data.get('Program_Id', chat.Program_Id)
                chat.Category_id = data.get('Category_id', chat.Category_id)
                db.session.commit()
                return jsonify({'message': 'Chat updated successfully!', 'chat': chat.as_dict()})
            else:
                return jsonify({'error': 'Chat not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def delete_chat(cid):
        try:
            chat = Chat.query.filter_by(isDeleted=False,id=cid).first()
            if chat:
                chat.isDeleted=True
                db.session.commit()
                return jsonify({'message': 'Chat deleted successfully!'})
            else:
                return jsonify({'error': 'Chat not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500


    @staticmethod
    def get_chats_by_person(person_id):
        try:
            chats = Chat.query.filter_by(Person_Id=person_id,isDeleted=False).all()
            return jsonify([chat.as_dict() for chat in chats])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def count_chats_by_person(person_id):
        try:
            total_chats = Chat.query.filter_by(Person_Id=person_id,isDeleted=False).count()
            return jsonify({'person_id': person_id, 'total_chats': total_chats})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def count_chats_by_program(program_id):
        try:

            total_chats = Chat.query.filter_by(Program_Id=program_id,isDeleted=False).count()
            return jsonify({'program_id': program_id, 'total_chats': total_chats})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def count_chats_by_session(session_id):
        try:
            total_chats = Chat.query.filter_by(Session_Id=session_id,isDeleted=False).count()
            return jsonify({'session_id': session_id, 'total_chats': total_chats})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def count_chats_by_category(category_id):
        try:
            total_chats = Chat.query.filter_by(Category_id=category_id,isDeleted=False).count()
            return jsonify({'category_id': category_id, 'total_chats': total_chats})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_chats_by_session(session_id):
        try:
            chats = Chat.query.filter_by(Session_Id=session_id).all()
            return jsonify([chat.as_dict() for chat in chats])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_chats_by_program(program_id):
        try:
            chats = Chat.query.filter_by(Program_Id=program_id).all()
            return jsonify([chat.as_dict() for chat in chats])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_chats_by_category(category_id):
        try:
            chats = Chat.query.filter_by(Category_id=category_id).all()
            return jsonify([chat.as_dict() for chat in chats])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def count_chats_by_session_title(session_title):
        try:
            total_chats = Chat.query.join(Session).filter(Session.title == session_title,Chat.isDeleted==False).count()
            return jsonify({'session_title': session_title, 'total_chats': total_chats})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_chats_of_all_persons_by_session_title(session_title):
        try:
            chats = Chat.query.join(Session).filter(Session.title == session_title).all()
            return jsonify([chat.as_dict() for chat in chats])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def categoryreport():
        try:
            # Query to count chats grouped by Category_id and include the category title
            category_counts = db.session.query(
                Chat.Category_id,
                func.count(Chat.id).label('total_chats'),
                Category.title
            ).join(Category).group_by(Chat.Category_id, Category.title).all()

            # Prepare the response
            return jsonify([{
                'category_id': category_id,
                'category_title': title,
                'total_chats': total_chats
            } for category_id, total_chats, title in category_counts])

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def categoryreportbyprogram(program_title):
        try:
            # Query to count chats grouped by Category_id and include the category title
            category_counts = db.session.query(
                Chat.Category_id,
                func.count(Chat.id).label('total_chats'),  # Use Chat.id if that's the correct field for counting
                Category.title
            ).join(Category).join(Program).filter(Program.name == program_title).group_by(Chat.Category_id,
                                                                                           Category.title).all()

            # Prepare the response
            return jsonify([{
                'category_id': category_id,
                'category_title': title,
                'total_chats': total_chats
            } for category_id, total_chats, title in category_counts])

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def sessionreport():
        try:
            session_counts = db.session.query(Chat.Session_Id, func.count(Chat.id), Session.title).join(
                Session).group_by(Chat.Session_Id, Session.title).all()

            return jsonify(
                [{'session_id': session_id, 'session_title': title, 'total_chats': count} for session_id, count, title
                 in session_counts])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def sessionreportbyprogram(program_title):
        try:
            print(f"Searching for program: {program_title}")
            session_counts = db.session.query(Chat.Session_Id, func.count(Chat.id), Session.title).join(
                Session).join(Program).filter(Program.name == program_title).group_by(Chat.Session_Id,
                                                                                      Session.title).all()

            if not session_counts:
                print("No sessions found for this program.")

            return jsonify(
                [
                    {'session_id': session_id, 'session_title': title, 'total_chats': count}
                    for session_id, count, title
                    in session_counts
                ])
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    # Additional Useful Actions

    @staticmethod
    def get_chat_summary():
        try:
            summary = db.session.query(
                func.count(Chat.id).label('total_chats'),
                func.count(func.distinct(Chat.Person_Id)).label('total_persons'),
                func.count(func.distinct(Chat.Session_Id)).label('total_sessions'),
                func.count(func.distinct(Chat.Program_Id)).label('total_programs'),
                func.count(func.distinct(Chat.Category_id)).label('total_categories')
            ).first()
            return jsonify({
                'total_chats': summary.total_chats,
                'total_persons': summary.total_persons,
                'total_sessions': summary.total_sessions,
                'total_programs': summary.total_programs,
                'total_categories': summary.total_categories
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    from datetime import datetime

    @staticmethod
    def get_chats_by_date_range(start_date, end_date):
        try:
            # Convert string dates to datetime objects if necessary
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date() if isinstance(start_date, str) else start_date
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date() if isinstance(end_date, str) else end_date

            # Query the database for chats within the given date range
            chats = Chat.query.filter(Chat.Date >= start_date, Chat.Date <= end_date,Chat.isDeleted==False).all()

            # Return the result as JSON
            return jsonify([chat.as_dict() for chat in chats])
        except Exception as e:
            return jsonify({'error': str(e)}), 500
