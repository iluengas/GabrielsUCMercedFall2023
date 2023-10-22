from myapp import db, User

#pulls all posts from py catagory 
    #Pulls all post rows in py table 
py.posts

#Pulls all posts belonging to py table that do not have the title: "Snake"
Post.query.with_parent(py).filter(Post.title != 'Snake').all()