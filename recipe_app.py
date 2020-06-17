# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:16:07 2020

@author: 212488697

Recipe app 
* users can input a recipe url and the app save the recipe to their name
* users can scale the recipe based on servings


code modified from http://introtopython.org/terminal_apps.html accessed 6/15/2020
"""
import os
import pickle
from pyfiglet import Figlet
import time

'''
TODO

[] login screen
[] main menu
[] recipe class
'''

### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('cls')
              
    print("\t*********************************************")
    print("\t***  Recipebook - Hello hungry friends!  ***")
    print("\t*********************************************")
    
def main_menu():
    # Let users know what they can do.
    print("\n[1] Login.")
    print("[2] New user.")
    print("[q] Quit.")
    
    return input("What would you like to do? ")
    
def login_menu():
    print("\n[1] View saved recipes.")
    print("[2] Add a recipe.")
    print("[q] Quit.")

    return input("What would you like to do? ")

def login():
   login_user = input("\nPlease enter your name: ") 
#   selection = ''
   if login_user in users:
       print("\nWelcome back %s!" % login_user)
#       selection = login_menu()
#       display_title_bar()
#       if selection == '1':
#           print("Here is a list of your saved recipes.")
#       elif selection == '2':
#           recipe_url = input("Please enter recipe URL: ")
#           print(recipe_url)
#       elif selection == 'q':
#           quit()
#       else:
#           print("\nI didn't understand that choice.\n")
   else:
       print("Sorry, I don't recognize that name. Please return to the main menu.")

def show_users():
    # Shows the names of everyone who is already in the list.
    print("\nHere are the people I know.\n")
    for name in users:
        print(name.title()) # title() returns first char in each word as uppercase and rest as lowercase
        
def get_new_user():
     # Asks the user for a new name, and stores the name if we don't already
    #  know about this person.
    new_user = input("\nPlease enter your name: ")
    if new_user in users:
        print("\n%s is already a user. Please login" % new_user.title())
    else:
        users.append(new_user)
        print("\nWelcome to the kitchen, %s!\n" % new_user.title())
    
def load_users():
    # This function loads names from a file, and puts them in the list 'names'.
    #  If the file doesn't exist, it creates an empty list.
    try:
        file_object = open('recipe-app_users.pydata', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names
    except Exception as e:
        print(e)
        return []

def quits():
    # This function dumps the names into a file, and prints a quit message.
    try:
        file_object = open('recipe-app_users.pydata', 'wb')
        pickle.dump(users, file_object)
        file_object.close()
        print("\nHappy eating! Bye.")
    except Exception as e:
        print("\nUh oh looks like there's a fire in the kitchen.")
        print(e)
        
### CLASSES ###

class Recipe:
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
login_lambda =   (lambda login: login())  

def menus(name):
    if name == 'main':
        return {'1': ['\n[1] Login.', {'action':login}],
          '2': ['[2] New user.', {'action':get_new_user}],
          'q': ['[q] Quit.', {'action':quits}]}
    elif name == 'login':
         return {'1': ['\n[1] New Recipe.', 'login'],
          '2': ['[2] View Recipes.', 'get_new_user'],
          'q': ['[q] Quit.', 'quit']},
    elif name == 'scale':
        {'1': ['\n[1] Save Recipe.', 'login'],
          '2': ['[2] Scale Recipe.', 'get_new_user'],
          'q': ['[q] Quit.', {'action':quits}]},
    elif name == 'select':
        {'1': ['\n[1] Select Recipe.', 'login'],
          'q': ['[q] Quit.', {'action':quits}]},
    elif name == 'edit':
         {'1': ['\n[1] Edit/Remove Recipe.', 'login'],
          '2': ['[2] Scale Recipe.', 'get_new_user'],
          'q': ['[q] Quit.', {'action':quits}]}   
    else:
        return print('\Error, %s not found' % name)


### MAIN PROGRAM ###   
            
os.system('cls')
f = Figlet(font='slant')
print(f.renderText('Recipebook'))
print("\nCreated by Sarah Morris, 2020.")
time.sleep(2)
  
users = load_users()

choice = ''
display_title_bar()
menu_location = 0
while choice != 'q':    
    # Let users know what they can do.
    for key, value in menus['main'].items():
        print(value[0])
    choice = input("What would you like to do? ")
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        print(menus['main']['1'][1]['action']())
        menus[menu_location]['1'][1]
        if menu_location >= len(menus):
            menu_location = 0
        else:
            menu_location += 1
    elif choice == '2':
        print(menus[menu_location]['2'][1]['action']())
    elif choice == 'q':
        quit()
    else:
        print("\nI didn't understand that choice.\n")
        
    
    