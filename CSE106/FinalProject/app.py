from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func,  select, and_
import json
from flask_login import LoginManager, current_user, login_user, login_required, logout_user, UserMixin, login_manager
from flask_bcrypt import Bcrypt 
import sqlite3
from sqlite3 import Error
from io import BytesIO
import base64


#Configure Flask app
app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

#Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db" 

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'redirectLoginPage'
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
            return self.id

class Users(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    bio = db.Column(db.String, nullable=False)
    profile_picture = db.Column(db.LargeBinary, nullable=False)
    creation_date = db.Column(db.String, nullable=False)
    views = db.Column(db.Integer)

class Posts(UserMixin, db.Model):
    postId = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    post_userID = db.Column(db.Integer)    
    post_textContent = db.Column(db.String)
    post_imageContent = db.Column(db.LargeBinary)
    post_creationDate = db.Column(db.String)
    post_likes = db.Column(db.Integer)  
    post_dislikes = db.Column(db.Integer)  
    parent_postID = db.Column(db.Integer)  

class PostTags(UserMixin, db.Model):
    rowID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    postID = db.Column(db.Integer, db.ForeignKey('posts.postId'), nullable=False)
    tagID = db.Column(db.Integer, db.ForeignKey('tags.tagID'), nullable=False)

    post = db.relationship('Posts', backref=db.backref('post_tags', lazy=True))
    tag = db.relationship('Tags', backref=db.backref('post_tags', lazy=True))


class Tags(UserMixin, db.Model):
    tagID = db.Column(db.Integer, primary_key=True)
    tagName = db.Column(db.String, unique=True)

class Likes(UserMixin, db.Model):
    l_rowID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    l_userID = db.Column(db.Integer)
    l_postID = db.Column(db.Integer)

class Dislikes(UserMixin, db.Model):
    d_rowID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    d_userID = db.Column(db.Integer)
    d_postID = db.Column(db.Integer)

class Bookmarks(UserMixin, db.Model):
    b_rowID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    b_postID = db.Column(db.Integer, nullable=False)
    b_userID = db.Column(db.Integer, nullable=False)

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
        return render_template("login_profile/login.html", error = error)
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
    return redirect(url_for('redirectLoginPage'))

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

            print("added accout")

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
    sql = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
            FROM Posts, Users 
            WHERE post_userID = user_id AND 
                    parent_postID IS NULL """
    
    tagQuery = """SELECT * 
                FROM Tags"""
    
    conn = openConnection(database)
    cur = conn.cursor()

        #Execute query and save all rows to a variable
    cur.execute(tagQuery)
    _tags = cur.fetchall()

        #Execute query and save all rows to a variable
    cur.execute(sql)
    _postData = cur.fetchall()


    if current_user.is_authenticated:
        return redirect(url_for('redirectFrontPageLoggedIn'))
    else:
        return render_template("frontPage.html", postData = _postData, tags = _tags)
    
@app.route("/redirectFrontPageLoggedIn", methods=['GET'])
@login_required
def redirectFrontPageLoggedIn():
    sql = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
            FROM Posts, Users 
            WHERE post_userID = user_id AND 
                    parent_postID IS NULL """
    
    tagQuery = """SELECT * 
                FROM Tags"""
    
    bookMarkQuery = """ SELECT * 
                        FROM Bookmarks
                            WHERE  b_userID = ?"""
    
    conn = openConnection(database)
    cur = conn.cursor()

        #Execute query and save all rows to a variable
    cur.execute(tagQuery)
    _tags = cur.fetchall()

        #Execute query and save all rows to a variable
    cur.execute(sql)
    _postData = cur.fetchall()

    cur.execute(bookMarkQuery, (current_user.id, ))
    _currentUsersBookmarkedPosts = cur.fetchall()

    return render_template("frontPage.html", postData = _postData, loggedIn = 1, tags = _tags, currentUsersBookmarkedPosts=_currentUsersBookmarkedPosts)

    
@app.route("/filterPosts", methods=['POST'])
def filterPosts():

    if request.method == 'POST':
        _filterTagID = request.form["filters"]

        if _filterTagID == 'all':
            return redirect(url_for('redirectFrontPage'))
        else:

            sql = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
                    FROM Posts, Users, 
                    (
                        SELECT postID as p_ID
                        FROM post_tags 
                        WHERE tagID = ?
                    )
                    WHERE postID = p_ID AND 
                            post_userID = user_id"""
            
            tagQuery = """SELECT * 
                        FROM Tags"""
            
            conn = openConnection(database)
            cur = conn.cursor()

                #Execute query and save all rows to a variable
            cur.execute(tagQuery)
            _tags = cur.fetchall()

                #Execute query and save all rows to a variable
            cur.execute(sql, (_filterTagID, ))
            _postData = cur.fetchall()

            tagRow = Tags.query.filter_by(tagID=_filterTagID).one()

            if current_user.is_authenticated:
                return render_template("frontPage.html", postData = _postData, loggedIn = 1, tags = _tags, filterTag = tagRow.tagName)
            else:
                return render_template("frontPage.html", postData = _postData, tags = _tags, filterTag = tagRow.tagName)
        
#Call this route to redirect to the create Post Page
    #tags will come as a tuple of tuples, including all data from tags table. This will be used to dynamically change the form
@app.route("/redirectCreatePost")
@login_required
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
@login_required
def createPost():

    if request.method == 'POST':
        _textContent = request.form['textContent'] 
        _imageContent = request.files['imageContent']

        postTags = request.form.getlist('postTags[]')
        print(_textContent)
        print(postTags)

        # Create the post in Posts table:
        sql = """INSERT INTO Posts(postID, post_userID, post_textContent,
                                    post_imageContent, post_creationDate,
                                    post_likes, post_dislikes, parent_postID)
                                VALUES(?, ?, ?, ?, datetime('now', 'localtime'), ?, ?, ?)"""
        
        if _imageContent is None:
            _imageData = None
        else: 
            _imageData = base64.b64encode(_imageContent.read()).decode('utf-8')
        
        _userID = current_user.id

        maxPostID = db.session.query(func.max(Posts.postId)).first()

        _postID = maxPostID[0] + 1


        args = [_postID, _userID, _textContent, _imageData, 0, 0, None]

        #Connect to DB and execute Sql -> Inputs new User to UserTable based on new account Creation
        conn = openConnection(database)
        conn.execute(sql, args)
        conn.commit()

        #Update tags table: 

        
        sql = """INSERT INTO post_tags(rowId, postID, tagID)
                                VALUES(?, ?, ?)"""
        
        for tag in postTags:
            maxRowQuery = """SELECT MAX(rowID) 
                    FROM post_tags"""
            
            conn = openConnection(database)
            cur = conn.cursor()
            cur.execute(maxRowQuery)
            _maxRow = cur.fetchall()

            args = [(_maxRow[0][0] + 1), _postID, tag]


            conn.execute(sql, args)
            conn.commit()
        
            
    
        return redirect(url_for('redirectFrontPage'))

@app.route("/createReplyPost/<_postID>", methods = ['GET', 'POST'])
@login_required
def createReplyPost(_postID):
    if request.method == 'POST':
        if current_user.is_authenticated:
            _textContent = request.form['textContent'] 
            _imageContent = request.files['imageContent']

            postTags = request.form.getlist('postTags[]')
            print(_textContent)
            print(postTags)

            # Create the post in Posts table:
            sql = """INSERT INTO Posts(postID, post_userID, post_textContent,
                                        post_imageContent, post_creationDate,
                                        post_likes, post_dislikes, parent_postID)
                                    VALUES(?, ?, ?, ?, datetime('now', 'localtime'), ?, ?, ?)"""
            
            if _imageContent is None:
                _imageData = None
            else: 
                _imageData = base64.b64encode(_imageContent.read()).decode('utf-8')

            _userID = current_user.id

            maxPostID = db.session.query(func.max(Posts.postId)).first()

            _postRowID = maxPostID[0] + 1


            args = [_postRowID, _userID, _textContent, _imageData, 0, 0, _postID]

            #Connect to DB and execute Sql -> Inputs new User to UserTable based on new account Creation
            conn = openConnection(database)
            conn.execute(sql, args)
            conn.commit()

            return redirect(url_for('redirectPostReplies',_postID=_postID))
        else:
            return redirect(url_for('redirectLoginPage'))


                

@app.route("/likePost/<_postID>", methods=['POST'])
@login_required
def likePost(_postID):
    
    if request.method == 'POST': 
        #Check if post is already liked by the current User
        likedQuery = """SELECT * 
                FROM Likes 
                WHERE l_userID = ? AND
                        l_postID = ?"""
        

        conn = openConnection(database)
        cur = conn.cursor()
        args = (current_user.id, _postID)
        cur.execute(likedQuery, args)
        alreadyLiked = cur.fetchall()

        #undo Like
        if alreadyLiked:
            # print(str(current_user.id) + " Already Liked Post-" + str(_postID))
        
            #Update Likes Table with user's ID and the post they're liking
            likeEntry = Likes.query.filter_by(l_userID = current_user.id, l_postID =_postID).one()
            db.session.delete(likeEntry)
            db.session.commit()

            #Decrement the post's post_likes entry in the Post Table
            likedPost = Posts.query.filter_by(postId=_postID).first()
            likedPost.post_likes -= 1
            db.session.commit()

            return str(likedPost.post_likes)
        
        #perform like
        else:
            #Create new row in the likes table
            newLikeEntry = Likes(l_userID = current_user.id, l_postID = _postID)

            with app.app_context():
                #Add new object to db
                db.session.add(newLikeEntry)
                    #Commit changes to db
                db.session.commit()

            likedPost = Posts.query.filter_by(postId=_postID).first()

            #Update Post.post_likes data and increment the count
            postToLike = Posts.query.filter_by(postId=_postID).first()

            postToLike.post_likes += 1
            db.session.commit()

            return str(likedPost.post_likes) 


@app.route("/checkIfDisliked/<_postID>", methods=['POST'])
@login_required
def checkIfDisliked(_postID):
    if request.method == 'POST': 
        sql = """SELECT * 
                FROM Dislikes 
                WHERE d_userID = ? AND 
                    d_postID = ? """
        
        conn = openConnection(database)
        cur = conn.cursor()
        args = (current_user.id, _postID)
        cur.execute(sql, args)
        alreadyDisliked = cur.fetchall()

        dislikedPost = Posts.query.filter_by(postId=_postID).first()

        if alreadyDisliked:
            #Clear row in dislikes table
            dislikeEntry = Dislikes.query.filter_by(d_userID = current_user.id, d_postID =_postID).one()
            db.session.delete(dislikeEntry)
            db.session.commit()

            #Decrement dislikes data from given post
            dislikedPost.post_dislikes -= 1
            db.session.commit()

        print("FROM CHECK IF Disliked (return dislikes): "+ str(dislikedPost.post_dislikes)) 

        return str(dislikedPost.post_dislikes)



@app.route("/dislikePost/<_postID>", methods=['POST'])
@login_required
def dislikePost(_postID):
    
    if request.method == 'POST': 

        #Check if post is already liked by the current User
        sql = """SELECT * 
                FROM Dislikes 
                WHERE d_userID = ? AND
                        d_postID = ?"""

        conn = openConnection(database)
        cur = conn.cursor()
        args = (current_user.id, _postID)
        cur.execute(sql, args)
        alreadyDislikes = cur.fetchall()

        #undo Like
        if alreadyDislikes:
            # print(str(current_user.id) + " Already Liked Post-" + str(_postID))
        
            #Update Likes Table with user's ID and the post they're liking
            dislikeEntry = Dislikes.query.filter_by(d_userID = current_user.id, d_postID =_postID).one()
            db.session.delete(dislikeEntry)
            db.session.commit()

            #Decrement the post's post_likes entry in the Post Table
            dislikedPost = Posts.query.filter_by(postId=_postID).first()
            dislikedPost.post_dislikes -= 1
            db.session.commit()

            return str(dislikedPost.post_dislikes)
        
        #perform like
        else:
            #Create new row in the likes table
            newDislikeEntry = Dislikes(d_userID = current_user.id, d_postID = _postID)

            with app.app_context():
                #Add new object to db
                db.session.add(newDislikeEntry)
                    #Commit changes to db
                db.session.commit()

            dislikedPost = Posts.query.filter_by(postId=_postID).first()

            #Update Post.post_likes data and increment the count
            PostToDislike = Posts.query.filter_by(postId=_postID).first()

            PostToDislike.post_dislikes += 1
            db.session.commit()

            return str(PostToDislike.post_dislikes) 

@app.route("/checkIfLiked/<_postID>", methods=['POST'])
@login_required
def checkIfLiked(_postID):
    if request.method == 'POST': 
        likedQuery = """SELECT * 
                FROM Likes 
                WHERE l_userID = ? AND
                        l_postID = ?"""
        

        conn = openConnection(database)
        cur = conn.cursor()
        args = (current_user.id, _postID)
        cur.execute(likedQuery, args)
        alreadyLiked = cur.fetchall()

        likedPost = Posts.query.filter_by(postId=_postID).first()
        #undo Like
        if alreadyLiked:
            # print(str(current_user.id) + " Already Liked Post-" + str(_postID))
        
            #Update Likes Table with user's ID and the post they're liking
            likeEntry = Likes.query.filter_by(l_userID = current_user.id, l_postID =_postID).one()
            db.session.delete(likeEntry)
            db.session.commit()

            #Decrement the post's post_likes entry in the Post Table
            likedPost.post_likes -= 1
            db.session.commit()

        print("FROM CHECK IF LIKED (return likes): " + str(likedPost.post_likes))    

        return str(likedPost.post_likes)

@app.route("/viewAccountInfo", methods=['GET'])
@login_required
def viewAccountInfo():

    _accountInfoQuery = Users.query.filter_by(user_id = current_user.id).one()

    _accountInfo = [_accountInfoQuery.user_id, _accountInfoQuery.username, _accountInfoQuery.bio, _accountInfoQuery.profile_picture, _accountInfoQuery.creation_date, _accountInfoQuery.views]

    return render_template("accountInfo/accountInfo.html", accountInfo = _accountInfo)

@app.route("/redirectEditUsername", methods=['GET'])
@login_required
def redirectEditUsername():
    return render_template("accountInfo/editUsername.html")

@app.route("/editUsername", methods=['POST'])
@login_required
def editUsername():

    if request.method == 'POST':
        _newUsername = request.form['newUsername']

        # Update the username in the database
        user = Users.query.filter_by(user_id=current_user.id).first()
        if user:
            user.username = _newUsername
            db.session.commit()

        return redirect(url_for('viewAccountInfo'))

@app.route("/redirectEditBio", methods=['GET'])
@login_required
def redirectEditBio():
    return render_template("accountInfo/editBio.html")

@app.route("/editBio", methods=['POST'])
@login_required
def editBio():

    if request.method == 'POST':
        _newBio = request.form['newBio'] 

        _currentUser = Users.query.filter_by(user_id = current_user.id).one()

        _currentUser.bio = _newBio

        db.session.commit()

        return redirect(url_for('viewAccountInfo'))

@app.route("/redirectEditPFP", methods=['GET'])
@login_required
def redirectEditPFP():
    return render_template("accountInfo/editPFP.html")

@app.route("/editPFP", methods=['POST'])
@login_required
def editPFP():

    if request.method == 'POST':
        _newPFP = request.files['newPfp'] 

        sql = """UPDATE Users
                    SET profile_picture = ?
                        WHERE user_id = ?"""

        conn = openConnection(database)
        cur = conn.cursor()
        args = [base64.b64encode(_newPFP.read()).decode('utf-8'), current_user.id]
        cur.execute(sql, args)
        conn.commit()

        # Update the profile_picture field in the Users table with binary data


        return redirect(url_for('viewAccountInfo'))
    
@app.route("/viewLikedPosts", methods=['GET'])
@login_required
def viewLikedPosts():

    sql = """SELECT postID, username, post_textContent,
                 post_imageContent, post_creationDate,
                   post_likes, post_dislikes, parent_postID, profile_picture
                    FROM Posts,
                    (
                        SELECT l_postID 
                        FROM likes
                        WHERE l_userID = ?
                    ), Users
                    WHERE postID = l_postID AND
                            post_userID ==  user_id"""
    
    bookMarkQuery = """ SELECT * 
                        FROM Bookmarks
                            WHERE  b_userID = ?"""
    
        # sql = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
        #     FROM Posts, Users WHERE post_userID = user_id"""

    conn = openConnection(database)
    cur = conn.cursor()

    args = (current_user.id, )
    cur.execute(sql, args)
    _postData = cur.fetchall()

    cur.execute(bookMarkQuery, (current_user.id, ))
    _currentUsersBookmarkedPosts = cur.fetchall()
    return render_template("accountInfo/viewLikedPosts.html", postData = _postData, currentUsersBookmarkedPosts=_currentUsersBookmarkedPosts)

@app.route("/viewDislikedPosts", methods=['GET'])
@login_required
def viewDislikedPosts():

    sql = """SELECT postID, username, post_textContent,
                 post_imageContent, post_creationDate,
                   post_likes, post_dislikes, parent_postID, profile_picture
                    FROM Posts,
                    (
                        SELECT d_postID 
                        FROM dislikes
                        WHERE d_userID = ?
                    ), Users
                    WHERE postID = d_postID AND
                            post_userID ==  user_id"""

    bookMarkQuery = """ SELECT * 
                        FROM Bookmarks
                            WHERE  b_userID = ?"""
    
        # sql = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
        #     FROM Posts, Users WHERE post_userID = user_id"""

    conn = openConnection(database)
    cur = conn.cursor()

    args = (current_user.id, )
    cur.execute(sql, args)
    _postData = cur.fetchall()

    cur.execute(bookMarkQuery, (current_user.id, ))
    _currentUsersBookmarkedPosts = cur.fetchall()

    return render_template("accountInfo/viewDislikedPosts.html", postData = _postData, currentUsersBookmarkedPosts=_currentUsersBookmarkedPosts)

@app.route("/redirectPostReplies/<_postID>", methods=['GET'])
def redirectPostReplies(_postID):
    headPostQuery = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
            FROM Posts, Users 
            WHERE post_userID = user_id AND 
                    postID = ?"""
    
    replyPostsQuery = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
                        FROM Posts, Users
                        WHERE post_userID = user_id AND 
                                parent_postID = ?"""
    

    
    conn = openConnection(database)
    cur = conn.cursor()

    args = (_postID, )

    cur.execute(headPostQuery, args)
    _headPost = cur.fetchall()

    cur.execute(replyPostsQuery, args)
    _replyPosts = cur.fetchall()

    print(replyPostsQuery)

    return render_template("postReplies.html", headPost = _headPost, replyPosts = _replyPosts)

@app.route("/viewMyPosts", methods=['GET'])
@login_required
def viewMyPosts():
    sql = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
            FROM Posts, Users 
            WHERE post_userID = user_id AND
                    post_userID = ? AND 
                    parent_postID IS NULL """
    
    conn = openConnection(database)
    cur = conn.cursor()
    args = (current_user.id, )
    cur.execute(sql, args)

    _postData = cur.fetchall()

    return render_template("accountInfo/viewMyPosts.html", postData = _postData)

@app.route("/viewMyReplies", methods=['GET'])
@login_required
def viewMyReplies():
    sql = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture, parent_postID
            FROM Posts, Users 
            WHERE post_userID = user_id AND
                    post_userID = ? AND 
                    parent_postID IS NOT NULL """
    
    conn = openConnection(database)
    cur = conn.cursor()
    args = (current_user.id, )
    cur.execute(sql, args)

    _postData = cur.fetchall()

    return render_template("accountInfo/viewMyReplies.html", postData = _postData)

@app.route("/addBookmark/<_postID>/<_pageFrom>", methods=['GET', 'POST'])
@login_required
def addBookmark(_postID, _pageFrom):
        print(_postID, current_user.id)
        alreadyBookmarked = Bookmarks.query.filter_by(b_postID = _postID, b_userID = current_user.id).first()

        if alreadyBookmarked:
            db.session.delete(alreadyBookmarked)
                            #Commit changes to db
            db.session.commit()
            flash('Post has been removed from bookmarks')
        else:
            newBookmark = Bookmarks(b_postID = _postID, b_userID = current_user.id)
        
                        #Add new object to db
            db.session.add(newBookmark)
                            #Commit changes to db
            db.session.commit()

            flash('Post has been bookmarked')



        if _pageFrom == "frontPage":
            return redirect(url_for('redirectFrontPage'))
        elif _pageFrom == "bookmarks":
            return redirect(url_for('viewMyBookmarks'))

        

@app.route("/viewMyBookmarks", methods=['GET'])
@login_required
def viewMyBookmarks():
    sql = """SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture, parent_postID
            FROM Posts, Users,
            (
                SELECT b_postID
                FROM Bookmarks 
                WHERE b_userID = ?
            ) 
            WHERE post_userID = user_id AND
                    postID = b_postID"""
    
    bookMarkQuery = """ SELECT * 
                        FROM Bookmarks
                            WHERE  b_userID = ?"""
    
    conn = openConnection(database)
    cur = conn.cursor()
    args = (current_user.id, )
    cur.execute(sql, args)
    _postData = cur.fetchall()

    cur.execute(bookMarkQuery, (current_user.id, ))
    _currentUsersBookmarkedPosts = cur.fetchall()

    return render_template("accountInfo/viewMyBookmarks.html", postData=_postData, currentUsersBookmarkedPosts=_currentUsersBookmarkedPosts)

@app.route("/redirectChangePassword", methods=['GET'])
@login_required
def redirectEditPassword():
    return render_template("accountInfo/editPassword.html")

@app.route("/changePassword", methods=['POST'])
@login_required
def changePassword():
    if request.method == 'POST':
        _oldPassword = request.form['oldPassword'] 
        _newPassword = request.form['newPassword'] 

        _currentUser = Users.query.filter_by(user_id = current_user.id).one()

        user = Logins.query.filter_by(id=current_user.id).first()

        if not user.check_password(_oldPassword):
            return render_template("accountInfo/editPassword.html", error = "Incorrect Password")
        
        else:
            user.password = bcrypt.generate_password_hash(_newPassword).decode('utf-8')
            db.session.commit()
            return redirect(url_for('viewAccountInfo'))
        
@app.route("/deletePost/<_postID>", methods=['GET'])
@login_required
def deletePost(_postID):
    #Check that post belongs to the current user 
        #if it does, delete it and commit db, renew post data, render myPost template

        #if NOT: return error message.3.
        sql = """DELETE FROM Posts WHERE postId = ?"""
        
        postData = Posts.query.filter_by(postId = _postID).one()

        if postData.post_userID == current_user.id:
            # db.session.delete(postData)
            # db.session.commit()
            conn = openConnection(database)
            cur = conn.cursor()
            cur.execute(sql, (_postID))
            conn.commit()
            return redirect(url_for('viewMyPosts'))
        else:
            return "That wasnt your post to delete"
        
@app.route("/deleteReply/<_postID>", methods=['GET'])
@login_required
def deleteReply(_postID):
    #Check that post belongs to the current user 
        #if it does, delete it and commit db, renew post data, render myPost template

        #if NOT: return error message.3.
        sql = """DELETE FROM Posts WHERE postId = ?"""
        
        postData = Posts.query.filter_by(postId = _postID).one()

        if postData.post_userID == current_user.id:
            # db.session.delete(postData)
            # db.session.commit()
            conn = openConnection(database)
            cur = conn.cursor()
            cur.execute(sql, (_postID))
            conn.commit()
            return redirect(url_for('viewMyReplies'))
        else:
            return "That wasnt your post to delete"
    




if __name__ == '__main__':
 app.run()
