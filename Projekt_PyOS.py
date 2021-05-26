import time
import json
import os
from art import *

def changeUsernameAndPassword():
    Userlogin = {"username": "admin", "password": "admin"}
    Userlogin["username"] = input("This will be your new Username!:  ")
    Userlogin["password"] = input("This will be your new Password!:  ")

    with open('userlogin.json', 'w') as f:
        json.dump(Userlogin, f)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Login():
    f = open('userlogin.json')
    Userlogin = json.load(f)
    while True:
            tprint("PyOS")
            usernameTry = input("Enter your Username:  ")
            passwordTry = input("Enter your Password:  ")
            clear()
            if usernameTry == Userlogin["username"] and passwordTry == Userlogin["password"]:
                break
            else:
                print("Wrong Username and/or Password . . .\nTry again!")
                time.sleep(2)
        


if __name__ == "__main__":
    clear()
    tprint("PyOS")
    time.sleep(3)
    if os.path.exists("userlogin.json") == False:
        changeUsernameAndPassword()
        
    Login()

    ans=True
    while ans: 
        print ("""
        1.Add a Student
        2.Delete a Student
        3.Look Up Student Record
        4.Exit/Quit
        """)
        ans=input("What would you like to do? ") 
        if ans=="1": 
            print("\n Student Added") 
        elif ans=="2":
            print("\n Student Deleted") 
        elif ans=="3":
            print("\n Student Record Found") 
        elif ans=="4":
            print("\n Goodbye") 
        elif ans !="":
            print("\n Not Valid Choice Try again")