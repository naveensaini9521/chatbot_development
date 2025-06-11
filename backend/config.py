import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'chatbot.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY", "secret")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")
