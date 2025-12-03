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


        
#init list full of courses
courses = [] #make each entry a dictionary with course info

#init a dictionary that holds registered courses and acts like a schedule
registered_courses = { "M" : [], "T" : [], "W" : [], "R" : [], "F" : [] } #lists act as a schedule for each day of the week

#function to add a course to the dictionary
def add_course(teach_status):
    #if the student is not a teacher, they cannot add courses
    if teach_status == False:
        return print("Students cannot add courses.")
    
    #input course info
    course_name = input("Enter course name: ")
    crn = input ("Enter course CRN: ")
    days = input("Enter days the course meets (e.g., MWF, TR): ")
    time = input("Enter time the course meets (e.g., 12:00-13:15): ")
    seats = input("Enter number of available seats: ")
    
    #create course dictionary and add to courses list
    courses.append({"name" : course_name, "CRN" : crn, "Days" : days, "Time" : time, "Seats" : seats})





user_creation()