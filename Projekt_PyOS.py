# Importere time.sleep funktionen
import time
# Til at lagre variabler til næste "boot" (brugernavn og password)
import json
# Bruges til at have muligheden for at clear terminalen
import os
# Importere random funktionen til Guessing_Game
import random
# Kan generere terminal art
from art import *

# Denne funktion bruges til at skifte password
def changeUsernameAndPassword():
    Userlogin = {"username": "admin", "password": "admin"}
    Userlogin["username"] = input("This will be your new Username!:  ")
    Userlogin["password"] = input("This will be your new Password!:  ")

    with open('userlogin.json', 'w') as f:
        json.dump(Userlogin, f)

# Cleare terminalen, fundet på stackoverflow
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Login funktionen der henter username og password fra json fil
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

# Den gyldne plug and play funktion for at lave menuer hurgtigt og nemt
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

# Lommeregner menu
def Calculator():
    global listofoptions
    clear()
    tprint("PyOS")
    listofoptions = [Plus,Minus,Multiply,Divide,MainMenu]


def Settings():
    global listofoptions
    listofoptions = [Login,changeUsernameAndPassword,ShutDown,MainMenu]

def ShutDown():
    quit()

def MainMenu():
    global listofoptions
    listofoptions = [Games,Calculator,Settings]
    
def Plus():
    MATH("+")

def Minus():
    MATH("-")
    
def Multiply():
    MATH("*")
    
def Divide():
    MATH("/")
    
def MATH(function):
    while True:
        try:
            clear()
            tprint("PyOS")
            firstnum = input("\nInput the first number: ")
            secondnum = input("\nInput the second number: ")
            firstnum = int(firstnum)
            secondnum = int(secondnum)

            if function == "+":
                result = firstnum + secondnum
            elif function == "-":
                result = firstnum - secondnum
            elif function == "*":
                result = firstnum * secondnum
            elif function == "/":
                result = firstnum / secondnum
            print("the result is: "+ str(result))
            input("Press enter to continue")
            break
        except ValueError:
            print("Wrong input, please try again . . .")
            time.sleep(2)
            continue


def Games():
    global listofoptions
    listofoptions = [Number_Guessing_Game,MainMenu]

def CheckForExistingLogin():
    if os.path.exists("userlogin.json") == False:
        changeUsernameAndPassword()       
    Login()

def Number_Guessing_Game():
    clear()
    tprint("PyOS")
    ans = None
    randomnr = random.randint(1,10)
    while True:
        try:
            clear()
            tprint("PyOS")
            print("\nThe number will be from 1-10")
            ans = int(input("\nGuess the number! "))
            if ans == randomnr:
                print("You guessed the number!")
                time.sleep(2)
                break
            else:
                print("Wrong number, try again!")
                input("Press enter to try again! . . .")
        except ValueError:
            print("Please write a number . . .")
            continue

if __name__ == "__main__":
    clear()
    tprint("PyOS")
    time.sleep(3)
    CheckForExistingLogin()
    mainMenuList = [Games,Calculator,Settings]
    listofoptions = mainMenuList
    menu()