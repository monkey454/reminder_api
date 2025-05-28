from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
from ..extensions import db
from ..models.reminder import Reminder
from datetime import datetime

reminder_parser = reqparse.RequestParser()
reminder_parser.add_argument('title', type=str, required=True, help='Title is required')
reminder_parser.add_argument('description', type=str)
reminder_parser.add_argument('due_date', type=str, required=True, help='due_date in ISO format required')
reminder_parser.add_argument('is_done', type=bool)

class ReminderListAPI(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        reminders = Reminder.query.filter_by(user_id=user_id).all()
        return [r.to_dict() for r in reminders], 200

    @jwt_required()
    def post(self):
        args = reminder_parser.parse_args()
        user_id = get_jwt_identity()

        try:
            due_date = datetime.fromisoformat(args['due_date'])
        except Exception:
            return {'message': 'Invalid due_date format, use ISO format'}, 400

        reminder = Reminder(
            title=args['title'],
            description=args.get('description'),
            due_date=due_date,
            is_done=args.get('is_done') or False,
            user_id=user_id
        )

        db.session.add(reminder)
        db.session.commit()

        return reminder.to_dict(), 201

class ReminderAPI(Resource):
    @jwt_required()
    def get(self, reminder_id):
        user_id = get_jwt_identity()
        reminder = Reminder.query.filter_by(id=reminder_id, user_id=user_id).first()
        if not reminder:
            return {'message': 'Reminder not found'}, 404
        return reminder.to_dict()

    @jwt_required()
    def patch(self, reminder_id):
        user_id = get_jwt_identity()
        reminder = Reminder.query.filter_by(id=reminder_id, user_id=user_id).first()

        if not reminder:
            return {'message': 'Reminder not found'}, 404

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('due_date', type=str)
        parser.add_argument('is_done', type=bool)
        args = parser.parse_args()

        if args['title'] is not None:
            reminder.title = args['title']
        if args['description'] is not None:
            reminder.description = args['description']
        if args['due_date'] is not None:
            try:
                reminder.due_date = datetime.fromisoformat(args['due_date'])
            except Exception:
                return {'message': 'Invalid due_date format'}, 400
        if args['is_done'] is not None:
            reminder.is_done = args['is_done']

        db.session.commit()
        return reminder.to_dict(), 200

    @jwt_required()
    def delete(self, reminder_id):
        user_id = get_jwt_identity()
        reminder = Reminder.query.filter_by(id=reminder_id, user_id=user_id).first()

        if not reminder:
            return {'message': 'Reminder not found'}, 404

        db.session.delete(reminder)
        db.session.commit()

        return {'message': 'Reminder deleted successfully'}, 200
