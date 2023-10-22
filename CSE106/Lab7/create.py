from lab7 import db, app
with app.app_context():
    db.create_all()