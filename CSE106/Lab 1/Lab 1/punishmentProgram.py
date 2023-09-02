def main():
    lineToRepeat = None
    repetitions = None

    while (lineToRepeat == None):
        (lineToRepeat) = str(input("Please enter the sentence to repeat: "))


    while (repetitions == None):
        try: 
            repetitions = int(input("Please enter the number if times this line should be repeated: "))
        except:
            print("Input must be an integer: ")
            repetitions = None


    f = open("CompletedPunishment.txt", "w")
    for x in range(repetitions):
        #print(lineToRepeat)
        f.write(lineToRepeat + "\n")

    f.close()     

if __name__ == '__main__':
    main()