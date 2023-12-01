from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func,  select, and_
import json
from flask_login import LoginManager, current_user, login_user, login_required, logout_user, UserMixin, login_manager
from flask_bcrypt import Bcrypt 
import sqlite3
from sqlite3 import Error
import cv2
import base64


#Configure Flask app
app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

#Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db" 

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = "strong"

database = r"instance/main.db"

app.secret_key = 'keep it secret, keep it safe' # Add this to avoid an error

#set db variable as a SQLAlchemy obj tied to flask app "app"
db = SQLAlchemy(app) 

#Users DB - Contains ids, usernames, and passwords.
class Logins(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
        email = db.Column(db.String, unique=True, nullable=False)
        password = db.Column(db.String, nullable=False)

        #Function to check hashed password for validity -> used in /login
        def check_password(self, password):
            return bcrypt.check_password_hash(self.password, password)
        
        #Function to return the ID of the current user 
        def get_id(self):
           return (self.id)
        
        #How the object is represented on call
        def __repr__(self):
            return self.username

#enables us to call current user
@login_manager.user_loader
def load_user(id):
    return db.session.get(Logins, id)

def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)


#Landing Page route, will go to login page
@app.route('/')
def home():
        #Display html file (**All html's go in templates -> CSS & JS go in static)
        return redirect(url_for('redirectFrontPage'))

#Landing Page route, will go to login page
@app.route('/redirectLoginPage')
def redirectLoginPage():
        #Display html file (**All html's go in templates -> CSS & JS go in static)
        return render_template("login_profile/login.html")


# #Route to handle login
    #Routes to /redirectFrontPage on successful login
@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None
    _username = request.form['name']
    _password = request.form['password']

    if current_user.is_authenticated:
        return redirect(url_for('redirectFrontPage'))
    user = Logins.query.filter_by(email=_username).first()
    if user is None or not user.check_password(_password):
        error = "Invalid Username or Password"
        flash("Incorrect Username or password")
        return render_template("login.html", error = error)
    else:
        login_user(user)
        next_page = request.args.get('next')
        return redirect(url_for('redirectFrontPage'))

@app.route('/signUp')
def signUp():
    return render_template('login_profile/signUpForm.html')

# #Route to let current user log out 
    #Redirects to landing/login page
@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template("login.html")

#Recieves data from createUser.html- Updates Users table with new profile data 
    #Redirects back to homepage
@app.route("/createUser", methods=['GET', 'POST'])
@login_required
def createUser():

    if request.method == 'POST':
        _username = request.form['newUsername']
        _bio = request.form['bio']  
        _img = request.files['profilePicture']  

        #Type in raw Sql
        sql = """INSERT INTO Users(user_id, username, bio,
                        profile_picture, creation_date, views)
                    VALUES(?, ?, ?, ?, datetime('now', 'localtime'), 0);"""  
        

        #Get User ID
        _id = Logins.get_id(current_user)
        # print("ID" + str(_id))

        # Encode the file content as Base64
        encoded_image = base64.b64encode(_img.read()).decode('utf-8')

        #Define the arguments
        args = [_id, _username, _bio, encoded_image]

        #Connect to DB and execute Sql -> Inputs new User to UserTable based on new account Creation
        conn = openConnection(database)
        conn.execute(sql, args)
        conn.commit()
    
        return redirect(url_for('redirectFrontPage'))

#Receives data from Login.hmtl to create an account on the site
# #Redirects by default to createUser.html    
@app.route('/createAccount', methods=['POST'])
def createAccount():
     
     if request.method == 'POST':
        _email = request.form['newEmail']
        newPassword = request.form['newPassword']

        newPassword = bcrypt.generate_password_hash(newPassword).decode('utf-8') 

        with app.app_context():


            maxID = db.session.query(func.max(Logins.id)).first()
            #Create new Gradebook object with value arguments maxID[0] + 1
            newAccount = Logins(id = (maxID[0] + 1), email = _email, password=newPassword)

            #Add new object to db
            db.session.add(newAccount)

            #Commit changes to db
            db.session.commit()

            print("added accoutn")

        # print (_email + newPassword)

        user = Logins.query.filter_by(email=_email).first()
        login_user(user)

        # Redirects new users to create a profile
        return render_template("login_profile/createUser.html")

#Call this route to display all of the users 
    #allUsers will come as a tuple of tuples, including all data from Users table
@app.route("/displayAllUsers")
def display():

    #Type in raw sql 
    sql = """SELECT * FROM USERS"""

    #Connect to the database and cursor 
    conn = openConnection(database)
    cur = conn.cursor()

    #Execute query and save all rows to a variable
    cur.execute(sql)
    _allUsers = cur.fetchall()

    #Render the html page allUsers.html, page will recieve tuple of tuples as a variable and can be parsed through
    return render_template("allUsers.html", allUsers = _allUsers)

#Call this route to redirect to the front Page
    #postData will come as a tuple of tuples, including all data from Posts table
@app.route("/redirectFrontPage")
def redirectFrontPage():
    sql = """SELECT postID, username, post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes 
            FROM Posts, Users WHERE post_userID = user_id"""
    
    conn = openConnection(database)
    cur = conn.cursor()

        #Execute query and save all rows to a variable
    cur.execute(sql)
    _postData = cur.fetchall()

    if current_user.is_authenticated:
        return render_template("frontPage.html", postData = _postData, loggedIn = 1)
    else:
        return render_template("frontPage.html", postData = _postData)
    
#Call this route to redirect to the create Post Page
    #tags will come as a tuple of tuples, including all data from tags table. This will be used to dynamically change the form
@app.route("/redirectCreatePost")
def redirectCreatePost():
    sql = """SELECT * 
                FROM Tags"""
    
    conn = openConnection(database)
    cur = conn.cursor()

        #Execute query and save all rows to a variable
    cur.execute(sql)
    _tags = cur.fetchall()
    return render_template("createPost.html", tags = _tags)


#Route to confirm post creation -> Updates Posts table with form data from createPost.html
    #will redirect to front page
        ### WORK IN PROGRESS ###
@app.route("/createPost", methods = ['GET', 'POST'])
def createPost():
    if request.method == 'POST':
        _textContent = request.form['textContent'] 
        _imageContent = request.files['imageContent']

        postTags = request.form.getlist('postTags')
        print(_textContent)
        print(postTags)

    return render_template("/redirectCreatePost.html")



if __name__ == '__main__':
 app.run()