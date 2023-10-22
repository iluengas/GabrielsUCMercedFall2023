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
    grades = json.load(open('grades.json'))
   #print(grades)
    return jsonify(grades)

@app.route('/grades/<student_name>', methods=['GET'])
def getStudentGrade(student_name):
    
        returnDict = {}

        grades = json.load(open('grades.json'))

        if student_name in grades:
                return jsonify({student_name: grades[student_name]})




@app.route('/grades', methods=['POST'])
def createSutdent():

        if request.method == "POST":
                data = json.loads(request.data)

                newStudent = data['name']
                newGrade = data['grade']

                grades = json.load(open('grades.json'))

                grades[newStudent] = newGrade

                with open("grades.json", "w") as outfile: 
                        json.dump(grades, outfile)

                grades = json.load(open('grades.json'))

                # grades[data['name']] = data['grade']

                return jsonify(grades)

@app.route('/grades/<student_name>', methods=['DELETE'])
def deleteSutdent(student_name):
        
        if request.method == "DELETE":
                grades = json.load(open('grades.json'))

                del grades[student_name]

        with open("grades.json", "w") as outfile: 
                json.dump(grades, outfile)

        grades = json.load(open('grades.json'))

        return jsonify(grades)

@app.route('/grades/<student_name>', methods=['PUT'])
def editSutdentGrade(student_name):
        
        if request.method == "PUT":
                data = json.loads(request.data)

                newGrade = data['grade']
                grades = json.load(open('grades.json'))

                grades[student_name] = newGrade
                
                with open("grades.json", "w") as outfile: 
                        json.dump(grades, outfile)

                grades = json.load(open('grades.json'))

                return jsonify(grades)


       
    
    




if __name__ == '__main__':
	app.run()