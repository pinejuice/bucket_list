import sys
sys.dont_write_bytecode = True

from flask import request, url_for, redirect, current_app
from flask_login import login_user, logout_user

@current_app.route('/login')
def login():
    if valid():
        login_user(user)
        return redirect(request.args.get('next') or url_for('top'))

@current_app.route('/logout')
def logout():
    logout_user()
