import re

def main():

    queryWord = str(input("Enter the word you would like to search for: "))

    try: 
        with open("PythonSummary.txt",'r') as f:
           contents = f.read()
           res = re.sub(r'(\W+)', lambda x: ' '+x.group(0)+' ', contents).split()
    except: 
        print ("Python Summary file not found\n")

    matchingWordCount = 0
    for word in res:
        if word.lower() == queryWord.lower():
            matchingWordCount = matchingWordCount + 1
    
    print ("The word " + queryWord + " occurs " + str(matchingWordCount) + " times")

if __name__ == '__main__':
    main()