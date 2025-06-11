from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import ChatHistory, db, Product, User
import re

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('', methods=['POST'])
@jwt_required()
def chat():
    user_id = get_jwt_identity()
    user_message = request.json.get('message', '')

    # Very basic keyword handling
    response = "Sorry, I didn’t understand that. Can you ask about products?"
    if "laptop" in user_message.lower():
        product = Product.query.filter(Product.name.ilike("%laptop%")).first()
        if product:
            response = f"We have: {product.name} for ₹{product.price}"
        else:
            response = "No laptops found right now."
    elif "cheap" in user_message.lower():
        product = Product.query.order_by(Product.price.asc()).first()
        response = f"Cheapest: {product.name} - ₹{product.price}"

    chat_record = ChatHistory(
        user_id=user_id,
        message=user_message,
        response=response
    )
    db.session.add(chat_record)
    db.session.commit()

    return jsonify({'response': response})
