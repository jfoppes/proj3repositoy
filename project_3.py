#!/usr/bin/env python3
#Jacob Foppes Project 3 -Downtime Tracker

'''Downtime tracker will let authernicated useres openm the downtime tracking file and add a new line with the serice outage they are reporting '''
'''Login:
takes username and password inputs and refernces a dictionary of usernamaes/passwrods to allow or stop login '''
import time
credentials = {} #creates an empy dictionary 
with open("pwdfile.txt") as p: #open the creditial file
    for line in p:
        (usr,pw) = line.split() #take a line from crentials file and split it into 2 parts 
        credentials[(usr)]= pw #add the useranme and passwrod entry to the dictionary 


while True:
    print("\n Welcome to Downtime tracker. Please login \n")
    cusername = input("Enter your username: ") # Storeing username and password 
    cpassword = input("Enter your password: ")
    login = {
       cusername : cpassword
    }
    if cusername not in credentials:
        print("\n User not found. Try agian. \n")
        time.sleep(1)
    elif credentials[cusername] == cpassword: #checks username and passwrod againsts known good credentails to allow or stop login 
        print("\n Login Succesful \n")
        break
    else:
        print("\n Incorrect Login. Try agian. \n")
        time.sleep(1)
    
''' read and Write:
Opens a logbook file and takes user input to add to the log'''

while True:
    choice = input("Would you like toi view or report an outage? \n (Enter: View, Report or exit)\n").lower() 
    if choice == "view":
        log = open('outageLog.txt','r') # open log file adn print
        print("\n"+log.read()+"\n\n\n\n")
        log.close()
        time.sleep(1)
        continue
    elif choice =="report": # open log file and append user iunput 
        log = open('outageLog.txt','a')
        outage = input("Use the following format to your outage:Format : \n [Date/Time], Reason for outage, Actions Taken, Expected return of services \n EX:\n [15:14 4 May 2023] Power outage, Restored power, 30 mins\n")
        log.write("\n" + outage + "\n")
        print("Update Recived\n")
        time.sleep(1)
        log.close()
    elif choice == "exit":
        break
    else:
        print("Please enter a valid choice")    
    
    
