from flask import Blueprint, request, jsonify
from models import Product

product_bp = Blueprint('products', __name__)

@product_bp.route('', methods=['GET'])
def get_products():
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    query = Product.query

    if category:
        query = query.filter_by(category=category)
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    results = query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'category': p.category,
        'price': p.price,
        'stock': p.stock,
        'description': p.description
    } for p in results])
