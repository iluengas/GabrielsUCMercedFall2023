from lab7 import db, Gradebook, app

with app.app_context():
    finn = Gradebook(name = 'Finn', grade=30)

    db.session.add(finn)

    db.session.commit()