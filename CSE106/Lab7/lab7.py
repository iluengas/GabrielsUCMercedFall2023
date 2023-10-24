from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import json

#Configure Flask app
app = Flask(__name__)
CORS(app)

#Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite" 

#set db variable as a SQLAlchemy obj tied to flask app "app"
db = SQLAlchemy(app) 


#Enter schema for all tables in db
        #Interpreter will view this "table" as an object with various attributes 
class Gradebook(db.Model):
        name = db.Column(db.String, primary_key=True, unique=True, nullable=False)
        grade = db.Column(db.Integer, nullable=False)


#Funtion to convert SQL quereies (received as objects) to dictionaries we can parse
        #Recieves array of objects as result for SQL query with multiple lines, each line is an object in the array 
def showGradebookSelection(queryArr):
        returnDict = {}

        for student in queryArr: 
                returnDict[getattr(student, 'name')] = getattr(student, 'grade')

        return (returnDict)

#Flask app structure: 
        #index.js (Front-end) file includes all fetch requests we make to out server 
                #Includes fetch functions that receive JSON responses from the server and manipulates it however 
                        #In This case, the JSON responses are converted into HTML we append to index.html
        #lab7.py (Back-End) file acts as our server and contains all of the routes that determine what kind of response will be sent out based on request information
                #In this case, the server routes expect a few types of requestes
                        #GET: lets us retrieve data from our db, no request parsing needed
                        #<student_name> GET: we can send a variable through a url from a front-end request, we can use this variable however we like
                        #POST (w/request data): Post lets us add data to our DB
                                #We can intake the request data coming in as JSON and parse it with json.loads(request.data)
                        #PUT: Used when we want to manipulate/edit existing data 
                        #DELETE: Delete data from table 


#Default Route "Landing page"
@app.route('/')
def renderIndex():
        #Display html file (**All html's go in templates -> CSS & JS go in static)
        return render_template("index.html")

#/grades route - method=GET
#Retrieves all rows in table in db
@app.route('/grades', methods=['GET'])
def getGrades():

        #Query all rows in Gradebook table
        # # Returns an array of objects     
        queryArr = (Gradebook.query.all())

        #Parse array of objects into a dictionary 
                #jsonify dictionary and send it as a JSON response to the front end  
        return jsonify(showGradebookSelection(queryArr))

#/grades/<student_name> route
# Gets a specific row in db matching the <student_name> variable in the URL
@app.route('/grades/<student_name>', methods=['GET'])
def getStudentGrade(student_name):      #include variables in function arguments 

        #Use Query.filter by -> followed by whatever we cant our filter to be **Can be algebraic 
                #Student is returned as a Gradebook obj
        student = Gradebook.query.filter_by(name = student_name).first()

        #Initilize a dactionary to return our response through 
        returnDict = {}

        #Populate dictionary with data from Gradebook Obj
        returnDict[student.name] = student.grade

        #Return json if query was not empty 
        if student:
                return jsonify(returnDict)
        else:
                return


#/Grades, method=POST
@app.route('/grades', methods=['POST'])
def createSutdent():
        #Request method conditional **needed
        if request.method == "POST":

                #Load data from request in a json obj
                data = json.loads(request.data)

                #Parse request data into variables
                newStudentName = data['name']
                newStudentGrade = data['grade']

                #With statement needed to make alterations to db 
                with app.app_context():

                        #Create new Gradebook object with value arguments
                        newStudent = Gradebook(name = newStudentName, grade=newStudentGrade)

                        #Add new object to db
                        db.session.add(newStudent)

                        #Commit changes to db
                        db.session.commit()

                        print("added student")

                        #Return all GradeBook rows as json to front end 
                        return jsonify(showGradebookSelection(Gradebook.query.all()))

#/grades/<student_name>, method=DELETE Route
#Deletes a row from db given a name through URL
@app.route('/grades/<student_name>', methods=['DELETE'])
def deleteSutdent(student_name):
        
        if request.method == "DELETE":

                with app.app_context():

                        studentToDelete = Gradebook.query.filter_by(name = student_name).first()

                        if (studentToDelete):
                                db.session.delete(studentToDelete)
                                db.session.commit()
                                return jsonify(showGradebookSelection(Gradebook.query.all()))
                        else:
                               return

#/grades/<student_name>, method=PUT
#Edit row in db based on name received through URL
@app.route('/grades/<student_name>', methods=['PUT'])
def editSutdentGrade(student_name):
        
        if request.method == "PUT":

                #Parse data received through request 
                        #Name
                        #New Grade
                data = json.loads(request.data)

                #Assign variable to value of grade in request.
                newGrade = data['grade']

                #Query the Gradebook table for the first entry where the name matches the student_name argument 
                student = Gradebook.query.filter_by(name = student_name).first()

                #Assign the newGrade value from request data to the student object's grade attribute 
                student.grade = newGrade

                #Commit Changes
                db.session.commit()

                #Return whole table as JSON to front end 
                return jsonify(showGradebookSelection(Gradebook.query.all()))

if __name__ == '__main__':
 app.run()