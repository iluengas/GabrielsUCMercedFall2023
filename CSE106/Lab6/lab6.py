from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import json



app = Flask(__name__)
CORS(app)

@app.route('/')
def renderIndex():
        # Input: None
        #GET
        # Return: JSON of students with grades
        return render_template("index.html")

@app.route('/grades', methods=['GET'])
def getGrades():
        # Input: None
        #GET
        # Return: JSON of students with grades
    grades = json.load(open('/grades.json'))
    print(grades)
    return grades

@app.route('/grades/<student_name>')
def getStudentGrade():
        # GET /grades/<student name>
        # Input: None
        # Return: JSON of student with grades
    grades = json.load(open('/grades.json'))
    if id in grades:
        return {id: grades[id]}




if __name__ == '__main__':
	app.run()