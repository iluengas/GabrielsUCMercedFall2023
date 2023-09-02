import json

def createStudent():
    x = 1

def askForGrade():
    x = 1

def editGrade():
    x = 1

def deleteGrade():
    x = 1

def main():

    with open ("grades.txt", "r") as jsonfile:
        students = json.load(jsonfile)
        print(students["John Smith"])

    print("Grading Program:\n Options:")
    print("(0) - Create Student Name & Grade \t (1) - Ask for grade \t (2) - Edit a Grade \t (3) - Delete a Grade")

    x = 0
    while True:
        option = input("Please select an option: ", int)

        if (option == 0):
            createStudent()
        elif (option == 1):
            askForGrade()
        elif (option == 2):
            editGrade()
        elif (option == 3):
            deleteGrade()
        else:
            print("ERROR - Unkown option selected")

if __name__ == '__main__':
    main()