from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db  # ✅ Correct usage
from routes.auth import auth_bp
from routes.products import product_bp
from routes.chat import chat_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app)
db.init_app(app)

jwt = JWTManager(app)

# Register routes
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(product_bp, url_prefix='/api/products')
app.register_blueprint(chat_bp, url_prefix='/api/chat')

@app.route('/')
def index():
    return {'message': 'API working'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
