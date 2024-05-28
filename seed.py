# seed.py

from app import create_app, db
from app.models.user_model import User
from app.models.email_model import Email

app = create_app()

with app.app_context():
    # Drop all tables and recreate them (useful for development purposes)
    db.drop_all()
    db.create_all()

    # Create sample users
    user1 = User(username='john_doe', email='john@example.com')
    user2 = User(username='jane_doe', email='jane@example.com')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Create sample emails linked to users
    email1 = Email(email='john.doe@example.com', user_id=user1.id)
    email2 = Email(email='jane.doe@example.com', user_id=user2.id)
    email3 = Email(email='john.personal@example.com', user_id=user1.id)

    db.session.add(email1)
    db.session.add(email2)
    db.session.add(email3)
    db.session.commit()

    print("Database seeded!")
