#function to find all classes student is registered for

def read_registered_classes(nuid, registered_classes):
#open file containing registrations
    register_file = open("registeredclass.txt", "r")

    #take all classes that the user is registered for and put 
    #them in the registered_classes list
    readregister = register_file.readlines()

    #track what line we are on
    file_line = 0

    while file_line < len(readregister):

        current_line = readregister[file_line]

        #import class info from the registrations file for the user
        if current_line[0:7] == str(nuid):   #find the nuid of the user

            #read the line after the nuid
            next_line = file_line + 1

            #read the next lines
            while next_line < len(readregister):
                class_line = readregister[next_line]

                #if the line is "*", break the loop
                if class_line.strip() == "*":
                    break

                #if the line is the nuid
                elif class_line.strip() == str(nuid):
                    next_line += 1
                    continue

                #split the line into its components
                desc = class_line.strip().split("\\")
                
                class_info = {
                    "name": desc[0],   
                    "department": desc[1],
                    "course number": desc[2],
                    "crn": desc[3],
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
                
                #update counter
                next_line += 1

            break

        #update file line counter
        file_line += 1

    register_file.close()

    return registered_classes

#function to read classes from file
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
                "filled seats": int(description[6]),
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
    print("add func called")

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

    #open file to write updated registrations
    register_file = open("registeredclass.txt", "w")

    #find nuid
    for line in lines:
        if line.strip() == str(nuid):

            nuid_line = lines.index(line)

            #start of class lines
            i = nuid_line + 1

            #put lines into updated lines until "*" is found
            while i < len(lines) and lines[i].strip() != "*":
                updated_lines.append(lines[i].strip())
                i += 1

            #delete old class lines
            del lines[nuid_line+1:i]

            #put classes back into position 
            position = nuid_line + 1
            
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

    #ask the user if they know the info of the class they want to add
    search_term = input("Enter the name, department, course number, " \
    "CRN, instructor, days, start time, end time, or location of the class" \
    " you want to add: \n")

    #search loop
    while True:
        #variable that says whether or not classes are found
        classes_found = False

        #search function
        while classes_found == False: #until classes are found
            found_classes = search(classes, search_term) #searches for classes based on user input

            #if classes are found
            if found_classes != []: #as long as the found classes list is not empty
                classes_found = True
            else: #if no classes are found
                #tell the user search failed
                print("No classes found matching that search term. Try again.\n")

                #ask the user to enter a new search term
                search_term = input("Enter the name, department, course number, " \
                "CRN, instructor, days, start time, end time, or location of the class" \
                " you want to add: \n")



        #displays found classes to user
        print("Found Classes:\n") #print the header

        #label the printed class with a number
        printed_class = {}

        #print 5 found classes
        print_count = 1

        #class that user wants to ad
        view_class = None

        while True:
            for classes_item in found_classes:
                if print_count < 6:
                    
                    #print class details
                    print(f"{print_count}. {classes_item['department']} {classes_item['course number']} {classes_item['name']} \
                    {classes_item['days']}  {classes_item['time start']} - {classes_item['time end']} Location: {classes_item['location']}")

                    #add the printed class to the dictionary
                    printed_class[print_count] = classes_item

                    print_count += 1

                #valid input check
                    valid = False

                while valid == False:

                    valid = True

                    #ask user to choose the course they want to look at or if they want to see more
                    view_more = input("Type the # next to the class or type 'more' to see more results:"
                    " or if you want to search again, type 'search': \n")

                    

                    #if the user found the class they want to look at
                    if view_more != "more" and view_more != "search" and view_more.isdigit() == True: #if user typed a class number
                        view_class = int(view_more)
                    elif view_more != "more" and view_more != "search" and view_more.isdigit() == False: #if user typed something invalid
                        print("Invalid input. Please try again.\n")

                        valid = False #input is invalid, repeat loop
                    

                #reset print count to print 5 more
                if view_more == "more": 
                    print("More Classes:\n") #print the header
                    print_count = 1
                elif view_more == "search": #if the user wants to search again
                    search_term = input("Enter the name, department, course number, " \
                    "CRN, instructor, days, start time, end time, or location of the class" \
                    " you want to add: \n")
                    print_count = 1
                    break

                else:
                    break
            break

        if view_more != "search":
            break  # Exit the outer while True loop

    #if the user selected a class to add
    if view_class != None:
        add_class(nuid, printed_class[view_class], registered_classes)
        print("Class added successfully!")

    return 

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
            

registered_classes = [] #list to store registered classes

classes = [] #list to store all classes

read_classes(classes)

read_registered_classes(2392262, registered_classes)

register(2392262, classes, registered_classes)