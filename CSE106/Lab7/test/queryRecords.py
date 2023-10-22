from myapp import db, User

peter = User.query.filter_by(username='Peter').first()

#Return id of peter 
peter.id

#Return email of peter 
peter.email 

##Can pull columns from row that query satisfies 
    #Can use like an object so we can manipulate data 

sam = User.query.filter_by(username = 'same').first()

#We can use a condictional statement to check if a querey came up positive/negative 
sam is None