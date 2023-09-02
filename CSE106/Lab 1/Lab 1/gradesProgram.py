import json

def createStudent(students):
    newStudent = str(input("Please enter the NEW student's name: "))

    while True:
        try:
            newGrade = float(input("Please enter the NEW student's grade: "))

            if int(newGrade) in range(1,101):
                students[newStudent] = newGrade
                print("NEW STUDENT ADDED")
                break
            else:
                print("Only float values within range 1-100 will be accepted.")
            pass
        except:
            print("Only float values will be accepted.")
            pass
            
def askForGrade(students):
    while True:
        studentQuery = (str(input("Enter the student name to VIEW grade: ")))

        try:
            print(studentQuery + "'s Grade: " + str(students[studentQuery]))
            break
        except:
            print("Student name not found, enter different name.")
            pass

def editGrade(students):
    while True:
        studentQuery = (str(input("Enter the student name to EDIT grade: ")))
        try:
            students[studentQuery]

            while True:
                try:
                    newGrade = float(input("Please enter the student's NEW GRADE: "))

                    if int(newGrade) in range(1,101):
                        students[studentQuery] = newGrade
                        print("GRADE CHANGED")
                        break
                    else:
                        print("Only float values within range 1-100 will be accepted.")
                        pass
                except:
                    print("Only float values will be accepted.")
                    pass
            break

        except:
            print("Student NAME NOT FOUND, enter different name.")
            pass

def deleteGrade(students):
    while True:
        studentQuery = (str(input("Enter the student name to DELETE grade: ")))

        try:
            del(students[studentQuery])
            print("STUDENT DELETED")
            break
        except:
            print("Student name not found, enter different name.")
            pass

def updateGradesJson(updatedStudents):
    with open("grades.txt", "w") as outfile:
        json.dump(updatedStudents, outfile)

def main():
    students = {}

    print("Grading Program:\n Options:")
    print("(0) - Create Student Name & Grade \t (1) - Ask for grade \t (2) - Edit a Grade \t (3) - Delete a Grade")
 
    while True:
        with open ("grades.txt") as jsonfile:
            students = json.load(jsonfile)

        option = (input("Please select an option: "))

        try: 
            if (int(option) == 0):
                createStudent(students)
                updateGradesJson(students)
                pass

            elif (int(option) == 1):
                askForGrade(students)
                pass

            elif (int(option) == 2):
                editGrade(students)
                updateGradesJson(students)
                pass

            elif (int(option) == 3):
                deleteGrade(students)
                updateGradesJson(students)
                pass

            else:
                print("ERROR - Unkown option selected")
                pass

        except:
            print("ERROR - Unkown option selected")
            pass

if __name__ == '__main__':
    main()