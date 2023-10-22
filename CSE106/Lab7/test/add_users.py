from myapp import db, User
#import db/user objects to allow us to manipulate data in main app

#Define new object and assign attributes 
admin = User(username="admin", email = "admin@gmail.com")

#Define new object and assign attributes 
guest = User(username="guest", email = "guest@gmail.com")

#.session -> opens a "session" that lets us manipulate the DB
    #.add() -> lets us add an object to a table object as a row 
db.session.add(admin)
db.session.add(guest)

#.commit() -> finalize transactions-> will happpen at the same time when we commit 
db.session.commit()