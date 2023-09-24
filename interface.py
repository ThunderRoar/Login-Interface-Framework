"""
Gateway of program
"""

from replit import clear
from time import sleep
import tester
from stdiomask import getpass
from colorama import Fore, Style, init
import json # Reference from w3schools.com

init(autoreset=True) # Resets the color of the text at the end of print statement 
attempt = 1    # Used in the login page for security pause
timeLock = 30  # Used in the login page for security pause

# READS THE TEXT FILE TO THE USERNAME AND PASSWORD LIST ###################

def Load():
  with open("Database/username.txt", "r") as f:
    try:
      tester.username_list = json.loads(f.read())
    except:
      pass
  
  with open("Database/password.txt", "r") as f:
    try:
      tester.password_list = json.loads(f.read())
    except:
      pass

# INTRO SCREEN ##########################################

# ASCII art 
def introDisplay():
  print('''

                    ───────────▀▄
                    ──█▄▄▄▄▄███▀▄─▄▄
                    ▄▀  ▀▄─▀▀█▀▀▄▀  ▀▄
                    ▀▄▀▀█▀▀████─▀▄  ▄▀
                    ──▀▀──────────▀▀──
                ██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██
                 █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
                 █░░║║║╠─║─║─║║║║║╠─░░█
                 █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
                ██▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██
  ''')
  sleep(2.25)
  clear()
  welcomeDisplay()

# WELCOME PAGE ##########################################

def welcomeDisplay():
  print('{:^}'.format("-"*60))
  print('{:^60}'.format("---| WELCOME TO THE WEBSITE |---"))
  print('{:^}'.format("-"*60))
  print()
  print('Enter 1 to \'SIGN UP\' as a new user')
  print('Enter 2 to \'LOG IN\' if you have an account')
  print()
  print('Number of users:', len(tester.username_list))
  print('{:^60}'.format("-"*60))
  print()
  userChoise = input("Your option 1 or 2: ")
  
  # Navigation menu route for website. Either to login page or sign up page
  if userChoise == '1':
    clear()
    for i in range(1, 4):
      print()
      print()
      print('{:^60}'.format("Loading"+"."*i))
      sleep(1)
      clear()
    register()
  elif userChoise == '2':
    clear()
    for i in range(1, 4):
      print()
      print()
      print('{:^60}'.format("Loading"+"."*i))
      sleep(1)
      clear()
    login()
  else:
    print()
    print(Fore.RED+'Invalid Input!! Please try again...')
    sleep(1.5)
    clear()
    welcomeDisplay()

# LOGIN PAGE ############################################

def login():
   print('{:^}'.format("-"*60))
   print('{:^60}'.format('-~/| LOGIN PAGE |\~-'))
   print('{:^}'.format("-"*60))
   print()
   global attempt
   print('{:>60}'.format("Attempt: "+str(attempt)))
   
   usernameExisting = input("Enter your Username: ")
   passwordExisting = getpass("Enter your Password: ")
   
   # variable check is a tuple
   global check
   check = tester.verify(usernameExisting, passwordExisting)

   # If check is true and matches the username and password for that account, it proceeds to homepage
   if check[0] == True:
     clear()
     attempt = 1
     homepage(usernameExisting)
   else:
     attempt += 1
     # Pauses the program for 30 seconds as security
     if attempt > 3:
       print()
       print(Fore.RED+"You have tried too many times. Returning to main page...")
       sleep(timeLock)   #obtains value from top of program
       clear()
       attempt = 1
       welcomeDisplay()
     else:
       print()
       print(Fore.RED+"Invalid password or username. Try again!")
       sleep(1)
       clear()
       login()
   
# REGISTER ##############################################

def register():
   print('{:^}'.format("-"*60))
   print('{:^60}'.format('---| CREATE A NEW ACCOUNT |---'))
   print('{:^}'.format("-"*60))
   print()
   print("-> Username should not have special character and should not")
   print("   be more than 15 characters.")
   print()
   print("-> Password must contain a special character, numbers,")
   print("   upper or lower case alphabets and the length of the")
   print("   password should be more than 5 characters.")
   print()
   print('{:^}'.format("-"*60))
   print()

   usernameNew = input("Create a Username: ")
   passwordNew = input("Your Password: ")

   # Checks the requirements for username and password to register, then writes it a file if it passes all the conditions
   test = tester.specialCharacter(usernameNew, passwordNew)
   if test == True:
     register()
   elif test == False:
     tester.username_list.append(usernameNew)
     tester.password_list.append(passwordNew)
   
   with open("Database/username.txt", "w") as file:
     file.write(json.dumps(tester.username_list))
   
   with open("Database/password.txt", "w") as file:
     file.write(json.dumps(tester.password_list))

   print()
   sleep(0.25)
   print(Fore.GREEN+'''
     |-------------------------------------------------|
     |  You have successfully created your account!!!  |
     |                                                 |
     |  To ensure successful login, the website will   |
     |  teleport you to the login page...              |
     |-------------------------------------------------|''')
   sleep(5)
   clear()
   login()

# HOMEPAGE ############################################

def homepage(usernameExisting):
   print('{:^}'.format("-"*60))
   print('{:^60}'.format('---| WELCOME TO HOMEPAGE |---'))
   print('{:^}'.format("-"*60))
   print()
   print('{:^66}'.format(Style.BRIGHT+'Website undergoing contruction...'))
   print()

   # Prints the user's account information
   profile()

   print()
   print('{:^}'.format("-"*60))
   print()
   print("Options:")
   print("Enter 1 to logout")
   print("Enter 2 to delete account")

   print('''
                     ───────────▀▄
                     ──█▄▄▄▄▄███▀▄─▄▄
                     ▄▀  ▀▄─▀▀█▀▀▄▀  ▀▄
                     ▀▄▀▀█▀▀████─▀▄  ▄▀
                    ───▀▀──────────▀▀───
   ''')
  
   userChoice = input("Your choice: ")

   # Handles the user input of logging out or deleting account and then send the user back to the welcome page. It also updates the website's Database.
   if tester.userDecision(userChoice, usernameExisting) == True:
     welcomeDisplay()
   elif tester.userDecision(userChoice, usernameExisting) == False:
    
    with open("Database/username.txt", "w") as file:
     file.write(json.dumps(tester.username_list))

    with open("Database/password.txt", "w") as file:
     file.write(json.dumps(tester.password_list))
    
    print(Fore.GREEN+"You have successfully deleted your account!")
    sleep(2.75)
    clear()
    for i in range(1, 4):
       print()
       print()
       print('{:^60}'.format("Logging Out"+"."*i))
       sleep(1.05)
       clear()
    # After deletion of account, it returns the user to the welcome page of the website
    welcomeDisplay()
   else:
     print(tester.userDecision(userChoice, usernameExisting))
     sleep(1.5)
     clear()
     homepage(usernameExisting)
  
   # Log off choise and brings user back to welcome page
   # userChoice = input("Do you want to logout (Y or N)? ")
  #  if tester.userDecision(userChoice) == True:
  #    welcomeDisplay()
  #  elif tester.userDecision(userChoice) == False:
  #    clear()
  #    homepage()
  #  else:
  #    print(tester.userDecision(userChoice))
  #    sleep(1.5)
  #    clear()
  #    homepage()

# PROFILE PAGE ############################################

def profile():
  # Reads the the username and password list upon login and prints it the Homepage under account information
  print(Style.DIM+"Account Information:")
  try:
    print(Style.DIM+"Username:", Style.DIM+tester.username_list[check[1]])
    print(Style.DIM+"Password:", Style.DIM+tester.password_list[check[1]])
  except:
    pass


