# Brady Yip
# EECE 2140 Final Project
# Created 12/3/2025 
# Northeastern Course Registration System



def read_registered_classes(nuid, registered_classes):

    registered_classes = []

    #credits counter
    credits = 0

    #open file containing registrations
    register_file = open(str(nuid)+".txt", "r")

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

                #if the line is not a comment line with a # or the name line with !
                if readregister[next_line].strip().startswith("#") or readregister[next_line].startswith("!"):
                    next_line += 1
                    continue

                class_line = readregister[next_line]

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

                #add to credit counter
                credits += int(desc[10])

            break

        #update file line counter
        file_line += 1

    register_file.close()

    return registered_classes, credits



#reads classes from classes.txt
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
                "filled seats": int(description[6]),
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
def add_class(nuid, reg_class, registered_classes, rosters):

    #calculate how many credits the user is currently registered for
    current_credits = 0
    for class_item in registered_classes:
        current_credits += class_item["credits"]

    #check if the class is already registered
    for class_item in registered_classes:
        if class_item["crn"] == reg_class["crn"]:
            return print("\nError: You are already registered for this class.")

    #check if adding the class would exceed 13 credits
    if current_credits >= 13:
        #print error message
        return print("\nError: Cannot register for more than 13 credits.")
    
    #check if the class is full
    if len(rosters[str(reg_class["crn"])]) >= reg_class["seats"]:
        #print error
        return print("\nError: Class is Full")

    #add the class they want to add to the list
    register_file = open(str(nuid)+".txt","a")

    #append the class
    line_to_add = f"{reg_class['name']}\\{reg_class['department']}\\{reg_class['course number']}\\{reg_class['crn']}\\{reg_class['instructor']}\\{reg_class['seats']}\\{reg_class['filled seats']}\\{reg_class['days']}\\{reg_class['time start']}\\{reg_class['time end']}\\{reg_class['credits']}\\{reg_class['location']}\n"
    register_file.write(line_to_add)
    register_file.close()

    return print("\nClass added successfully.")



#function to drop classes
def drop_class(nuid, drop_crn,):

    #open file containing registrations
    register_file = open(str(nuid)+".txt", "r")

    #read all lines from the file
    readregister = register_file.readlines()

    #close the file
    register_file.close()

    for lines in readregister:

        #find the class that matches the crn to be dropped
        if lines[0:7] == str(nuid):   #find the nuid of the user

            #read the line after the nuid
            next_line = readregister.index(lines) + 1

            #read the next lines
            while next_line < len(readregister):
                class_line = readregister[next_line]

                #split the line into its components
                desc = class_line.strip().split("\\")

                #check if the crn matches
                if desc[3] == drop_crn:
                    #remove this line from the list
                    readregister.pop(next_line)
                    break

                #update counter
                next_line += 1

            break

    #write the updated registrations back to the file
    register_file = open(str(nuid)+".txt", "w")
    register_file.writelines(readregister)
    register_file.close()

    #return success message
    return print("Dropped Successfully.")



#prints registered classes
def print_registered_classes(registered_classes, credits):

    #print total credits
    print("Total Credits Registered:", credits)

    #counter to count number of classes printed
    i = 1

    #print results
    for class_item in registered_classes:

        print(f"{i}. {class_item["department"]} {class_item["course number"]} {class_item["name"]}  CRN: {class_item["crn"]} \
            Instructor: {class_item["instructor"]} Days: {class_item["days"]} Time: {class_item["time start"]}-{class_item["time end"]} \
            Credits: {class_item["credits"]} Location: {class_item["location"]}\n")
        
        #add to counter
        i += 1

    return



#function to store people in class rosters
def roster(classes):

    #create a dictionary to store the students in each class
    rosters = {}

    #fill dictionary with crns
    for class_item in classes:

        #each entry in rosters is a crn key with a list of nuids
        rosters[class_item["crn"]] = []

    #scan every registry file 
    for nuid in range(1000000,1000010): #nuids are 7 digits long if you want to check every nuid replace second num with 10^8

        #open file with the nuid in the title and read it
        try: #if a nuid file doesnt exist skip it
            registry_file = open(str(nuid)+".txt","r")
        except FileNotFoundError:
            continue

        lines = registry_file.readlines()
        registry_file.close()

        #track what line we are on
        file_line = 0

        while file_line < len(lines):

            current_line = lines[file_line]

            #import class info from the registrations file for the user
            if current_line[0:7] == str(nuid):   #find the nuid of the user

                #read the line after the nuid
                next_line = file_line + 1

                #read the next lines
                while next_line < len(lines):

                    #if the line is not a comment line with a # or the name line with !
                    if lines[next_line].strip().startswith("#") or lines[next_line].strip() == "!":
                        next_line += 1
                        continue

                    class_line = lines[next_line]

                    #split the line into its components
                    desc = class_line.strip().split("\\")

                    #if the line is less than it should be
                    if len(desc) < 4:
                        next_line += 1
                        continue
                    
                    #find the crn
                    crn = desc[3]

                    next_line += 1

                    #add the nuid to the roster list for the corresponding crn
                    rosters[crn].append(nuid)

    

                break

            #update file line counter
            file_line += 1
    
    #add the number of filled seats to the class
    for class_item in classes:
        #take the length of the list in roster and add it as the filled seats vallue in classes
        crn = class_item["crn"]
        class_item["filled seats"] = len(rosters[crn])

    return rosters



#function to display the roster
def disp_roster(rosters, crn):

    #list containing all the names in the course
    names = []
    
    #get the list of nuids for the class
    for nuid in rosters[crn]:

        #open the corresponding registry file and find the name
        registry_file = open(str(nuid)+".txt", "r")
        lines = registry_file.readlines()
        
        #read every line
        for line in lines:

            #if the line starts with !
            if line.startswith("!"):
                #take away the ! and append the name
                name = line.strip("!")
                names.append(name)
                break
    
    #print each name
    for name in names:
        print(f"\n{name}")





#start of main

#initialize variables
classes = []
registered_classes = []
credits = 0
rosters = {}

#read classes from classes.txt
classes = read_classes(classes)

#create rosters for each class
rosters = roster(classes)

#greet user
print("Welcome to the Northeastern Course Registration System!\n")

#create user profile
#ask for nuid
nuid = input("Please enter your NUID to continue: ")

#skip a lines to cleanup ui
print("\n")

#read registered classes
registered_classes, credits = read_registered_classes(nuid, registered_classes)

#print classes registered
print_registered_classes(registered_classes, credits)

#ask user what they want to do 
action = input("\nWould you like to (S)earch for classes, (A)dd a class, (D)rop a class: ")

#while the user is still using the application
while 1:

    #if user wants to exit program
    if action.lower() == "e":
        print("\nThank you for using the Northeastern Course Registration System. Goodbye!")
        break

    #while user wants to search for classes
    while action.lower() == "s":
        #ask user for search term
        search_term = input("\nEnter a search term (department, course number, instructor, days, time, location): ")

        #search for classes
        found_classes = search(classes, search_term)

        #print found classes
        if len(found_classes) == 0:
            print("\nNo classes found matching your search term.") #no classes found error search agian
        
        else:
            #print each class
            print("\nFound Classes:")

            #counter to put a number next to each class
            print_count = 1

            #dictionary so the user can select which class to add
            class_dict = {}

            for class_info in found_classes:
                print(f"{print_count}. {class_info['department']} {class_info['course_number']} {class_info['name']}  CRN: {class_info['crn']} \
                    Instructor: {class_info['instructor']} Days: {class_info['days']} Time: {class_info['time_start']}-{class_info['time_end']} \
                    Credits: {class_info['credits']} Location: {class_info['location']}")
                
                #add class to dictionary with number as key
                class_dict.update({print_count: class_info})

                #increment counter
                print_count += 1

            #get the class the user wants to view
            view_key = int(input("\nWhich class would you like to view?: "))

            #print info and roster
            print(class_dict[view_key])
            disp_roster(rosters, class_dict[view_key]["crn"])

            #ask user if they want to add this class
            add_choice = input("\nWould you like to add this class? (Y/N)")

            #if yes ask for the number next to the class
            if add_choice.lower() == "y":

                #add the class
                add_class(nuid, class_dict[view_key], registered_classes,rosters)

                #display updated registered classes
                registered_classes, credits = read_registered_classes(nuid, registered_classes)
                print("\n")
                print_registered_classes(registered_classes, credits)

                print("\n")

        #ask user what they want to do next
        action = input("\nWould you like to (S)earch for classes, (A)dd a class, (D)rop a class, (E)xit: ")

    #while user wants to add a class
    while action.lower() == "a":
        #ask user for search term
        search_term = input("\nEnter a search term (department, course number, instructor, days, time, location, CRN): ")

        #search for classes
        found_classes = search(classes, search_term)

        #print found classes
        if len(found_classes) == 0:
            print("\nNo classes found matching your search term.") #no classes found error search agian
        
        else:
            #print each class
            print("\nFound Classes:")

            #counter to put a number next to each class
            print_count = 1

            #dictionary so the user can select which class to add
            class_dict = {}

            for class_info in found_classes:
                print(f"{print_count}. {print_count}. {class_info['department']} {class_info['course_number']} {class_info['name']}  CRN: {class_info['crn']} \
                    Instructor: {class_info['instructor']} Days: {class_info['days']} Time: {class_info['time_start']}-{class_info['time_end']} \
                    Credits: {class_info['credits']} Location: {class_info['location']}")
                
                #add class to dictionary with number as key
                class_dict.update({print_count: class_info})

                #increment counter
                print_count += 1

        #ask user which class they want to add or search again
        choice = input("\nEnter the number next to the class you want to add or S to search again: ")

        if choice.lower() != "s":
            keynum = int(choice)

            #add the class
            add_class(nuid, class_dict[keynum], registered_classes)

            #display updated registered classes
            registered_classes, credits = read_registered_classes(nuid, registered_classes)

        #if user wants to search again
        else: 
            continue

        print("\n")

        #ask user what they want to do next
        action = input("\nWould you like to (S)earch for classes, (A)dd a class, (D)rop a class, (E)xit: ")

    #while user wants to drop a class
    while action.lower() == "d":

        #ask user which class to drop
        drop_crn = input("\nEnter the CRN of the class you want to drop: ")

        #drop the class
        drop_class(nuid, drop_crn)

        #display updated registered classes
        registered_classes, credits = read_registered_classes(nuid, registered_classes)
        print("\n")
        print_registered_classes(registered_classes, credits)
        print("\n")

        #ask user what they want to do next
        action = input("\nWould you like to (S)earch for classes, (A)dd a class, (D)rop a class, (E)xit: ")
