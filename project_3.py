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
        print("\n Login Succesfull \n")
        break
    else:
        print("\n Incorrect Login. Try agian. \n")
        time.sleep(1)
    
''' Write:
Opens a logbook file and takes user input to add to the log'''



#choice = choice.lower()
while True:
    choice = input("Would you like toi view or report an outage? \n (Enter: View, or Report)\n").lower()
    if choice == "view":
        log = open('outageLog.txt','r')
        print("\n"+log.read()+"\n\n\n\n")
        continue
    elif choice =="report":
        log = open('outageLog.txt','w')
        outage = input("Use the following format to your outage:")
        log.write(outage)
    else:
        print("Please enter a valid choice")    
    
    
