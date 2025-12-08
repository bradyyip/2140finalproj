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

# #function to add a class
# def add_class(nuid, reg_class, classes, registered_classes):
#     #open file containing registered classes
#     register_file = open("registrations.txt", "w")

#     #add the class to the file
#     readregister



# #function to look at classes
# def register(nuid, classes, registered_classes):

#     #open file containing registrations
#     register_file = open("registrations.txt", "r")

#     #take all classes that the user is registered for and put 
#     #them in the registered_classes list
#     readregister = register_file.readlines()

#     for line in readregister:

#         #import class info from the registrations file for the user
#         if line[0:9] == nuid:   #find the nuid of the user

#             #read the next lines
#             for line in readregister:

#                 #if the line is "*", break the loop
#                 if line.strip() == "*":
#                     break

#                 #split the line into its components
#                 desc = line.strip().split("\\")

#                 class_info = {
#                     "name": desc[0],   
#                     "department": desc[1],
#                     "course_number": desc[2],
#                     "section": desc[3],
#                     "instructor": desc[4],
#                     "seats": int(desc[5]),
#                     "filled": int(desc[6]),
#                     "days": desc[7],
#                     "time_start": desc[8],
#                     "time_end": desc[9],
#                     "credits": int(desc[10]),
#                     "location": desc[11]
#                 }

#             registered_classes.append(class_info)
#     register_file.close()

#     #open registrations file in write mode
#     register_file = open("registrations.txt", "w")

#     #ask the user if they know the info of the class they want to add
#     search_term = input("Enter the name, department, course number, " \
#     "CRN, instructor, days, start time, end time, or location of the class" \
#     " you want to add: ")

#     #searches for classes based on user input
#     found_classes = search(classes, search_term)

#     #displays found classes to user
#     print("Found Classes:\n") #print the header
    
#     #print 5 found classes
#     print_count = 1
#     for classes in found_classes:
#         if print_count < 6:
            
#             #print class details
#             print(f"{print_count}. {classes['department']} {classes['name']} \
#             Starts: {classes['time_start']} Location: {classes['location']}")

#             #label the printed class with a number
#             printed_class = {print}

#             print_count += 1

#         #ask user to choose the course they want to look at or if they want to see more
#         view_more = input("Choose a class to view or type 'more' to see more results: ")

#         #if the user found the class they want to look at
#         if view_more != "more":
#             view_class = int(view_more)

#         #reset print count to print 5 more
#         if view_more == "more": 
#             print("More Classes:\n") #print the header
#             print_count = 1
#         else 

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
                "course number": description[2],
                "crn": description[3],
                "instructor": description[4],
                "seats": int(description[5]),
                "filled": int(description[6]),
                "days": description[7],
                "time start": description[8],
                "time end": description[9],
                "credits": int(description[10]),
                "location": description[11]

            }

            #add class info to classes list
            classes.append(class_info)

    #close file
    classefile.close()

    return classes



#function to add a class
def add_class(nuid, reg_class, registered_classes):

    #add new class to registered classes list
    registered_classes.append(reg_class)
    
    #open file containing registered classes
    register_file = open("registeredclass.txt","r")

    #read the file
    lines = register_file.readlines()
    
    #close the file to avoid unintended behavior
    register_file.close()

    #updated lines to write back to the file
    updated_lines = [reg_class]

    #find nuid
    for line in lines:
        if line.strip() == nuid:

            #start of class lines
            i = lines.index(line) + 1

            #put lines into updated lines until "*" is found
            while i < len(lines) and lines[i].strip() != "*":
                updated_lines.append(lines[i].strip())
                i += 1

            #delete old class lines
            del lines[lines.index(line)+1:i]

            #put classes back into position 
            position = lines.index(line) + 1
            
            #insert new class lines
            for class_dic in registered_classes:
                class_line = f"{class_dic['name']}\\{class_dic['department']}\\{class_dic['course number']}\\{class_dic['crn']}\\{class_dic['instructor']}\\{class_dic['seats']}\\{class_dic['filled seats']}\\{class_dic['days']}\\{class_dic['time start']}\\{class_dic['time end']}\\{class_dic['credits']}\\{class_dic['location']}\n"

                #insert class line at position
                lines.insert(position, class_line)
                position += 1

            break

    #write lines back to file
    register_file = open("registeredclass.txt","w")
    register_file.writelines(lines)
    register_file.close()

    return registered_classes
            
            
        
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
                    "course number": desc[2],
                    "section": desc[3],
                    "instructor": desc[4],
                    "seats": int(desc[5]),
                    "filled seats": int(desc[6]),
                    "days": desc[7],
                    "time start": desc[8],
                    "time end": desc[9],
                    "credits": int(desc[10]),
                    "location": desc[11]
                }

            registered_classes.append(class_info)
    register_file.close()

    #ask the user if they know the info of the class they want to add
    search_term = input("Enter the name, department, course number, " \
    "CRN, instructor, days, start time, end time, or location of the class" \
    " you want to add: ")

    #searches for classes based on user input
    found_classes = search(classes, search_term)

    #displays found classes to user
    print("Found Classes:\n") #print the header

    #label the printed class with a number
    printed_class = {}

    #print 5 found classes
    print_count = 1
    for classes in found_classes:
        if print_count < 6:
            
            #print class details
            print(f"{print_count}. {classes['department']} {classes['name']} \
            Starts: {classes['time_start']} Location: {classes['location']}")

            #add the printed class to the dictionary
            printed_class[print_count] = classes

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
        else:
            break

    add_class(nuid, printed_class[view_class], registered_classes)

    return print("Class added successfully!")

            

registered_classes = [] #list to store registered classes

classes = [] #list to store all classes

read_classes(classes)





