def main():
    raw_input = input("Please enter 2 or more integers separated by a space: ")

    str_list = raw_input.split()

    try:
        int_list = [eval(x) for x in str_list]
    except:
        print ("ERROR - Please only input integers!")
        str_list = []
        int_list = []
        main()
    else:
        sum = 0

        for x in int_list:
            sum += x

        print ("Total: ", sum)

if __name__ == '__main__':
    main()

