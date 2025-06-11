from faker import Faker
import random
from models import db, Product
from app import app

fake = Faker()

categories = ["Electronics", "Books", "Clothing", "Home", "Beauty", "Sports"]

def generate_products(n=100):
    for _ in range(n):
        product = Product(
            name=fake.catch_phrase(),
            category=random.choice(categories),
            price=round(random.uniform(10.0, 500.0), 2),
            stock=random.randint(5, 100),
            description=fake.text(max_nb_chars=200)
        )
        db.session.add(product)
    db.session.commit()
    print(f"{n} products added to the database.")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        generate_products()
