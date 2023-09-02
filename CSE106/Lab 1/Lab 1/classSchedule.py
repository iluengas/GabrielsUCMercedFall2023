import re

def main():

    lines = []

    try: 
        with open("classesInput.txt",'r') as f:
           for line in f:
                lines.append(line.strip())
    except: 
        print ("classesInput.txt file not found\n")

    numberOfClasses = int(lines[0])

    for x in range(numberOfClasses):
        print ("COURSE " + str(x+1) + ": " + (lines[1] + lines[2]) + ": " + lines[3])
        print ("Number of Credits: " + lines[4])
        print ("Days of Lectures: " + lines[5])
        print ("Lecture Time: " + lines[6] + " - " + lines[7])
        print ("Stat: on average, students get " + lines[8] + "% in this course") 
        print("\n")

        del lines[1:9]

if __name__ == '__main__':
    main()