from myapp import db, User
#import db and tables 

#Query all users 
User.query.all()

#will return all rows with username='admin'
User.query.filter_by(username="admin")

#will return FIRST row with username='admin'
User.query.filter_by(username="admin").first()

