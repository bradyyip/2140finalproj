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

classes = [] #list to store all classes

#read txt file that stores all classes
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
                "section": description[3],
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
    for list_entry in classes:
        for value in list_entry:
            if value == search_term:
                found_classes.append(list_entry)

    return found_classes

registered_classes = [] #list to store registered classes

#function to add a class
def add_class(nuid, classes, registered_classes):

    #open file containing registrations
    register_file = open("registrations.txt", "r")

    #take all classes that the user is registered for and put 
    #them in the registered_classes list
    readregister = register_file.readlines()

    for line in readregister:

        #import class info from the registrations file for the user
        if line[6:16] == nuid:
            description = line.strip().split("\\")

            class_info = {
                "name": description[0],
                "department": description[1],
                "course_number": description[2],
                "section": description[3],
                "instructor": description[4],
                "seats": int(description[5]),
                "filled": int(description[6]),
                "days": description[7],
                "time_start": description[8],
                "time_end": description[9],
                "credits": int(description[10]),
                "location": description[11]

            }

            registered_classes.append(class_info)
    register_file.close()

    #open registrations file in write mode
    register_file = open("registrations.txt", "w")

    #ask the user if they know the info of the class they want to add
    search_term = input("Enter the name, department, course number, " \
    "CRN, instructor, days, time_start, time_end, or location of the class" \
    " you want to add: ")

    found_classes = search(classes, search_term)



    #open registrations file in write mode
    #register_file = open("registrations.txt", "w")