import sys
sys.dont_write_bytecode = True

from flask import Flask
from flask_login import LoginManager

def create_app():
    # appの設定
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    # ロギングの設定


    # Blueprintの登録

    return app
