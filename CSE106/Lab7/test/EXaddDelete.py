from myapp import db, User

#Create new User "row"/Obj
me = User("admin", "gmail.com")

#add row object to db (will insert itself into respective table)
db.session.add(me)

#commit the change 
db.session.commit()

db.session.delete(me)
db.session.commit()