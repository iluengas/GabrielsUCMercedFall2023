from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite" 
db = SQLAlchemy(app) 

class Gradebook(db.Model):
        name = db.Column(db.String, primary_key=True, unique=True, nullable=False)
        grade = db.Column(db.Integer, nullable=False)

def showGradebookSelection(queryArr):
        returnDict = {}

        for student in queryArr: 
                returnDict[getattr(student, 'name')] = getattr(student, 'grade')

        return (returnDict)

@app.route('/')
def renderIndex():
        return render_template("index.html")

@app.route('/grades', methods=['GET'])
def getGrades():

        queryArr = (Gradebook.query.all())

        return jsonify(showGradebookSelection(queryArr))

@app.route('/grades/<student_name>', methods=['GET'])
def getStudentGrade(student_name):

        student = Gradebook.query.filter_by(name = student_name).first()

        returnDict = {}
        returnDict[student.name] = student.grade

        if student:
                return jsonify(returnDict)
        else:
                return


@app.route('/grades', methods=['POST'])
def createSutdent():

        if request.method == "POST":

                data = json.loads(request.data)

                newStudentName = data['name']
                newStudentGrade = data['grade']

                with app.app_context():
                        newStudent = Gradebook(name = newStudentName, grade=newStudentGrade)

                        db.session.add(newStudent)

                        db.session.commit()

                        print("added student")

                        return jsonify(showGradebookSelection(Gradebook.query.all()))


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


@app.route('/grades/<student_name>', methods=['PUT'])
def editSutdentGrade(student_name):
        
        if request.method == "PUT":
                data = json.loads(request.data)

                newGrade = data['grade']

                student = Gradebook.query.filter_by(name = student_name).first()

                student.grade = newGrade

                db.session.commit()

                return jsonify(showGradebookSelection(Gradebook.query.all()))

if __name__ == '__main__':
 app.run()