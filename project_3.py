#!/usr/bin/env python3
#Jacob Foppes Project 3 -Downtime Tracker

'''Downtime tracker will let authernicated useres openm the downtime tracking file and add a new line with the serice outage they are reporting  '''


'''Login:
takes username and password inputs and refernces a dictionary of usernamaes/passwrods to allow or stop login '''

credentials = {} #creates an empy dictionary 
with open("pwdfile.txt") as p: #open the creditial file
    for line in p:
        (usr,pw) = line.split() #take a line from crentials file and split it into 2 parts 
        credentials[(usr)]= pw #add the useranme and passwrod entry to the dictionary 


while True:
    print("Welcome to Downtime tracker. Please login")
    cusername = input("Enter your username") # Storeing username and password 
    cpassword = input("Enter your passwrod")
    login = {
       cusername : cpassword
    }
    if credentials[cusername] == cpassword: #checks username and passwrod againsts known good credentails to allow or stop login 
        print("Login Succesfull")
        break
    else:
        print("Incorrect Login. Try agian")
    
''' Write:
Opens a logbook file and takes user input to add to the log'''


