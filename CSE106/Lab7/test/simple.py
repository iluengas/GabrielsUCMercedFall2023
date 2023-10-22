from myapp import db, Category, Post

#Creates Python category obj
py = Category(name="Python")


#Create post obj with py category
Post(title="Hello Python", body = "Python Body", category=py)

#Post creation v.2: 
p = Post(title="Snakes", body="snake body")

#append post p to py category posts **Possible because of back-reference
py.posts.append(p)

db.session.add(py)