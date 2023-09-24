'''
Supports the interface program
'''

from replit import clear
from time import sleep
from colorama import Fore, init
init(autoreset=True) # Resets the color of the text at the end of print statement

username_list = []
password_list = []


#CHECKS THE USERNAME FOR SPECIAL CHARACTERS AND FOR DUPLICATE USERNAMES ##############################

def specialCharacter(usernameNew, passwordNew):
  specialChar_list = ['`', '~', '#', '%', '^', '*', '(', ')', '-', '_', '=', '+', '/', '\\', '|', '?', '<', '>', ';', ':', '@', '!', '&', '$']

  for i in range(len(usernameNew)):
    if usernameNew[i] in specialChar_list:
      print(Fore.RED+'Special characters not allowed in Username.')
      sleep(1.25)
      clear()
      return True
  if len(usernameNew) > 15:
    print(Fore.RED+'Username should be less than 15 chracters.')
    sleep(1.25)
    clear()
    return True

  # Checks to see there is no duplicate usernames
  elif usernameNew not in username_list:
    # Check the password now after the check for duplication of username
    if len(passwordNew) <= 5:
      print(Fore.RED+"Length of password should be greater than 5.")
      sleep(1.25)
      clear()
      return True
    #(passwordNew.isalnum()) != False # another way for checking of special character
    elif (any(element in specialChar_list for element in passwordNew)) != True:
      print(Fore.RED+"Password must contain special character.")
      sleep(1.25)
      clear()
      return True
    # Checks for numbers in the password
    elif (any(element.isdigit() for element in passwordNew)) != True:
       print(Fore.RED+"Password must contain numbers.")
       sleep(1.25)
       clear()
       return True
    else:
      return False
  else:
    print(Fore.RED+'Username already exists, try again.')
    sleep(1.5)
    clear()
    return True

# CHECKS THE USERNAME & PASSWORD OF USER FOR LOGIN ##################

def verify(usernameExisting, passwordExisting):
  for i in range(len(password_list)):
    if usernameExisting == username_list[i]:
      if passwordExisting == password_list[i]: 
        return True, i
  return False, ''

# CHOISE LOOP FOR LOGGING OFF FROM HOMEPAGE ###############

def userDecision(choise, account):
  if choise == '2':
    deleteAccount(account)
    return False
  elif choise == '1':
    sleep(1)
    clear()
    for i in range(1, 4):
       print()
       print()
       print('{:^60}'.format("Logging Out"+"."*i))
       sleep(1.05)
       clear()
    return True
  else:
    return (Fore.RED+'Invalid Input!')
 
# yes_list = ['yes', 'Yes', 'YES', 'Y', 'y']
# no_list = ['no', 'No', 'No', 'N', 'n']
# if choise in yes_list:
#   sleep(1.5)
#   clear()
#   for i in range(1, 4):
#      print()
#      print()
#      print('{:^60}'.format("Logging Out"+"."*i))
#      sleep(1.05)
#      clear()
#   return True
# elif choise in no_list:
#   return False
# else:
#   return (Fore.RED+'Invalid Input!')

# DELETE ACCOUNT #######################################

def deleteAccount(account):
  try:
    accountIndex = username_list.index(account)
    username_list.pop(accountIndex)
    password_list.pop(accountIndex)
  except:
    pass



