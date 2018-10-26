from pymongo import MongoClient
from datetime import datetime
#import json

student = MongoClient('localhost', 27017)
mydb = student.db_University

def add_student(student_name, student_age, student_roll_number, student_branch):
    unique_student= mydb.db_University.find_one({"Student Roll Number":student_roll_number}, {"_id":0})
    if unique_student:
        return "students already exists"
    else:
        mydb.db_University.insert(
                {
                "Student Name": student_name,
                "Student Age": student_age,
                "Student Roll Number": student_roll_number,
                "Student Branch": student_branch,
                "Date-Time":datetime.now()
                })
        return "students added successfully"

def view_student(student_roll_number):
    user = mydb.db_University.find_one({"Student Roll Number":student_roll_number}, {"_id":0})
    if user:
        student_name = user["Student Name"]
        student_age = user["Student Age"]
        student_roll_number = user["Student Roll Number"]
        student_branch = user["Student Branch"]
        time = user["Date-Time"]
        return {"Student Name":student_name,"Student age":student_age,"Student roll nunber":student_roll_number,"Student Branch":student_branch}
    else:
        return "Sorry, No such user exists"


student_name = raw_input("Student Name: ")
student_age = raw_input("Student Age: ")
student_roll_number = raw_input("Student Roll Number: ")
student_branch = raw_input("Student Branch: ")

print add_student(student_name, student_age, student_roll_number, student_branch)

user = raw_input("Enter Student roll number to find: ")
user_data = view_student(user)

print user_data