# Brady Yip
# EECE 2140 Final Project
# Created 12/3/2025 
# Northeastern Course Registration System



#create user profile
def user_creation():
    #is user student or teacher
    user_input = input("Student or Teacher? (S/T): ")
    if user_input == "S":
        teach = False
    elif user_input == "T":
        teach = True
    else:
        print("Invalid input. Please enter 'S' for Student or 'T' for Teacher.")
        return user_creation()
    
    #ask for name and id
    name = input("Enter your name: ")
    nuid = input("Enter your NUID number: ")

    return teach, nuid, name



def read_classes(classes):
    classefile = open("classes.txt", "r")
    readclass= classefile.readlines()

    #dont add any comments in the txt file to the classes list
    for line in readclass:

        #comments in txt file start with #
        #read only lines that dont start with #
        if not line.strip().startswith("#"):

            #each part of the description is separated by a backslash
            description = line.strip().split("\\")

            class_info = {
                "name": description[0],
                "department": description[1],
                "course_number": description[2],
                "crn": description[3],
                "instructor": description[4],
                "seats": int(description[5]),
                "filled": int(description[6]),
                "days": description[7],
                "time_start": description[8],
                "time_end": description[9],
                "credits": int(description[10]),
                "location": description[11]

            }

            #add class info to classes list
            classes.append(class_info)

    #close file
    classefile.close()

    return classes



#function that allows user to find class
def search(classes, search_term):

    #list to store found classes
    found_classes = []

    #search for classes based on search type
    for list_entry in classes: #for every class
        for value in list_entry.values(): #for every class attribute
            if search_term.lower() in str(value).lower(): #if the search term is in the attribute
                found_classes.append(list_entry) #add the class to found classes

    return found_classes



#function to add a class
def add_class(nuid, reg_class, classes, registered_classes):
    #open file containing registered classes
    register_file = open("registrations.txt", "w")

    #add the class to the file
    readregister



#function to look at classes
def register(nuid, classes, registered_classes):

    #open file containing registrations
    register_file = open("registeredclasses.txt", "r")

    #take all classes that the user is registered for and put 
    #them in the registered_classes list
    readregister = register_file.readlines()

    for line in readregister:

        #import class info from the registrations file for the user
        if line[0:9] == nuid:   #find the nuid of the user

            #read the next lines
            for line in readregister:

                #if the line is "*", break the loop
                if line.strip() == "*":
                    break

                #split the line into its components
                desc = line.strip().split("\\")

                class_info = {
                    "name": desc[0],   
                    "department": desc[1],
                    "course_number": desc[2],
                    "section": desc[3],
                    "instructor": desc[4],
                    "seats": int(desc[5]),
                    "filled": int(desc[6]),
                    "days": desc[7],
                    "time_start": desc[8],
                    "time_end": desc[9],
                    "credits": int(desc[10]),
                    "location": desc[11]
                }

            registered_classes.append(class_info)
    register_file.close()

    #open registrations file in write mode
    register_file = open("registrations.txt", "w")

    #ask the user if they know the info of the class they want to add
    search_term = input("Enter the name, department, course number, " \
    "CRN, instructor, days, start time, end time, or location of the class" \
    " you want to add: ")

    #searches for classes based on user input
    found_classes = search(classes, search_term)

    #displays found classes to user
    print("Found Classes:\n") #print the header
    
    #print 5 found classes
    print_count = 1
    for classes in found_classes:
        if print_count < 6:
            
            #print class details
            print(f"{print_count}. {classes['department']} {classes['name']} \
            Starts: {classes['time_start']} Location: {classes['location']}")

            #label the printed class with a number
            printed_class = {print}

            print_count += 1

        #ask user to choose the course they want to look at or if they want to see more
        view_more = input("Choose a class to view or type 'more' to see more results: ")

        #if the user found the class they want to look at
        if view_more != "more":
            view_class = int(view_more)

        #reset print count to print 5 more
        if view_more == "more": 
            print("More Classes:\n") #print the header
            print_count = 1
        else

    
classes = [] #list to store all classes

registered_classes = [] #list to store registered classes