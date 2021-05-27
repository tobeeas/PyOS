from random import choices
import time
import json
import os
from art import *

#This is a function
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
            clear()
            tprint("PyOS")
            usernameTry = input("Enter your Username:  ")
            passwordTry = input("Enter your Password:  ")
            clear()
            if usernameTry == Userlogin["username"] and passwordTry == Userlogin["password"]:
                break
            else:
                print("Wrong Username and/or Password . . .\nTry again!")
                time.sleep(2)
        
def printNonNoneChoice(chnr):
    chnr = "ch"+chnr
    if chnr != None:
        print(str(chnr)+". " + str((chnr)))

def menu():
    while True: 
        clear()
        tprint("PyOS")
        count = 1
        for functions in listofoptions:
           print(str(count)+". "+functions.__name__)
           count = count+1
        ans = input("\nWhat would you like to do? ")
        try:
            ans = int(ans)
            ans = ans-1
            listofoptions[ans]()
        except ValueError:
            print("Not a valid option, try again")
            time.sleep(2)
            clear()
            continue
        except IndexError:
            
            print("Not a valid option, try again")
            time.sleep(2)
            clear()
            continue

def Calculator():
    clear()
    print("Calculator")
    input("waiting")

if __name__ == "__main__":
    clear()
    tprint("PyOS")
    time.sleep(3)
    if os.path.exists("userlogin.json") == False:
        changeUsernameAndPassword()       
    Login()

    listofoptions = [Calculator,Login,changeUsernameAndPassword]
    menu()