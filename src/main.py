#!/usr/bin/python3
from datetime import timedelta

from flask import flash, Flask, jsonify, redirect, render_template, request, Response, send_file, send_from_directory, session, url_for
from flask_login import current_user, login_required, login_user, logout_user, LoginManager, UserMixin
from src.shared import User, list_users, list_processes,  check_password
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "c7d6ee3e38c6ce4c50aedeedcf622b9f"
app.app_context().push()
login_manager = LoginManager()
login_manager.init_app(app)
users = list_users()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/logout/")
@login_required
def logout():
    logout_user()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route("/api/login", methods=["POST"])
def login():
    log_data = json.loads(request.get_json(force=True))
    username = log_data['login']
    password = log_data['password']
    if check_password(username, password):
        user_to_login = None
        for user in users:
            if user.id() == username:
                user_to_login = user
                break
        if user_to_login is not None:
            login_user(user_to_login)
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        else:
            return json.dumps({'success': False}), 403, {'ContentType': 'application/json'}


@login_manager.user_loader
def load_user(user_id):
    global users
    for user in users:
        if user.id() == user_id:
            return user


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=15)
    session.modified = True

if __name__ == '__main__':
    app.run(debug=True)
