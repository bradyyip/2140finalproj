def read_registered_classes(nuid, registered_classes):

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

def print_registered_classes(registered_classes, credits):

    #print total credits
    print("Total Credits Registered:", credits)

    #counter to count number of classes printed
    i = 1

    #print results
    for classes in registered_classes:

        print(f"{i}. {classes["department"]} {classes["course number"]} {classes["name"]}  CRN: {classes["crn"]} \
            Instructor: {classes["instructor"]} Days: {classes["days"]} Time: {classes["time start"]}-{classes["time end"]} \
            Credits: {classes["credits"]} Location: {classes["location"]}")
        
        #add to counter
        i += 1

    return

#credits counter
credits = 0

registered_classes = []
registered_classes, credits = read_registered_classes(2392262, registered_classes)

print_registered_classes(registered_classes, credits)

drop_class(2392262, "15920")

registered_classes = []

registered_classes, credits = read_registered_classes(2392262, registered_classes)

print_registered_classes(registered_classes, credits)
