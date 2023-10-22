from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   #Create flask app called "app"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite" #Configure location of database -> can be local in folder OR URI
db = SQLAlchemy(app) #Creates db obj with sql-alchemy within app

#Create a table for "User" -> Interpreted as an object
class User(db.Model):
            #Define column -> define data type -> define key type/conditionals
    id = db.Column(db.Integer, primary_key=True)
                                                #Field Can't be null
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


#One to many relationship: one category to many posts 

from datetime import datetime
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
                                                        #Autosets the time to when post obj is created 
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
                                            #maps primary key of other table to represent reference 
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
                                        #Back Reference -> reference catagory through posts 
                                            #Lets us get list of all posts under a certain catergory -> <category>.posts
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))
    def __repr__(self):
        return '<Post %r>' % self.title
 

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Category %r>' % self.name 
    


#Many-to-many relationships, many pages have many tags (need a junction table)

    #Create connecting table with foreign keys referencing tables it is connecting 
tags = db.Table('tags',
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True)
)

#Page table 
class Page(db.Model):
        #Initialize page ID  
    id = db.Column(db.Integer, primary_key=True)
        #Create relationship between pages and tags 
            #Lets us get all pages under a certaing tag with <tag>.pages
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                            backref=db.backref('pages', lazy=True)) 
    
#Basic Tag table, with tag ids
class Tag(db.Model):
 id = db.Column(db.Integer, primary_key=True) 


