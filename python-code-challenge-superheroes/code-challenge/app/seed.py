from app import app, db  # Import your Flask app and SQLAlchemy instance
from models import Hero, Power

def create_tables():
    with app.app_context():
        # Create the database tables
        db.create_all()

def seed_database():
    with app.app_context():
        # Create instances of your models and add them to the database session
        power1 = Power(name="Super Strength")
        power2 = Power(name="Flight")
        power3 = Power(name="Telekinesis")

        hero1 = Hero(name="Superman", powers=[power1, power2])
        hero2 = Hero(name="Wonder Woman", powers=[power2])
        hero3 = Hero(name="Jean Grey", powers=[power3])

        db.session.add_all([power1, power2, power3, hero1, hero2, hero3])

        # Commit the changes to the database
        db.session.commit()

if __name__ == "__main__":
    create_tables()  # Create the database tables first
    seed_database()  # Seed the database with data
