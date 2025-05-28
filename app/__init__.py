from flask import Flask
from flask_restful import Api
from .extensions import db, jwt
from .routes.auth_routes import AuthRegisterAPI, AuthLoginAPI
from .routes.reminder_routes import ReminderListAPI, ReminderAPI

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reminder.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # change in prod!

    db.init_app(app)
    jwt.init_app(app)

    api = Api(app)

    # Auth endpoints
    api.add_resource(AuthRegisterAPI, '/auth/register')
    api.add_resource(AuthLoginAPI, '/auth/login')

    # Reminder endpoints
    api.add_resource(ReminderListAPI, '/reminders')
    api.add_resource(ReminderAPI, '/reminders/<int:reminder_id>')

    return app
