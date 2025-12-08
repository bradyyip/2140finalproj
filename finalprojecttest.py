#function to add a class
def add_class(nuid, classes, registered_classes):

    #open file containing registrations
    register_file = open("registrations.txt", "r")

    #take all classes that the user is registered for and put 
    #them in the registered_classes list
    readregister = register_file.readlines()

    for line in readregister:

        #import class info from the registrations file for the user
        if line[0:9] == nuid:
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