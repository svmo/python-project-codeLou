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
from recipe_scrapers import scrape_me

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
    
def login():
   login_user = input("\nPlease enter your name: ") 
   display_title_bar()
   if login_user in users:
       print("\nWelcome back %s!" % login_user)
       return True
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

def add_new_recipe():
    URL = input('What is the recipe URL? ')
    scraper = scrape_me(URL)
    display_title_bar()
    print('\n**' + scraper.title()+'**\n')
    print('INGREDIENTS')
    for ingredient in scraper.ingredients():
        print(ingredient)
    print('\nINSTRUCTIONS')
#    for instructions in scraper.instructions():
    print(scraper.instructions())
    return True
    
def save_recipe():
    print('This is where the user will be able to save a recipe')
    return True
    
def scale_recipe():
    print('This is where a user will be able to scale a recipe')
    return True
    
def edit_recipe():
    print('A user will be able to edit their recipe, maybe')
    return True
    
def delete_recipe():
    print('Delete recipes here')
    return True
    
def show_recipe_list():
    print('Show what recipes a user has, maybe select recipe too')
    return True
    
def select_recipe():
    print('User can select a recipe')
    return True

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
  

def menus(name):
    if name == 'main':
        return {'1': ['\n[1] Login.', {'action':login}, 'login'],
                '2': ['[2] New user.', {'action':get_new_user}, 'main'],
                'q': ['[q] Quit.', {'action':quits}]}
    elif name == 'login':
         return {'1': ['\n[1] New Recipe.', {'action':add_new_recipe}, 'scale'],
                 '2': ['[2] View Recipes.',{'action':show_recipe_list}, 'select'],
                 'q': ['[q] Quit.', {'action':quits}]}
    elif name == 'scale':
        return {'1': ['\n[1] Save Recipe.',{'action':save_recipe}, 'scale'],
                '2': ['[2] Scale Recipe.',{'action':scale_recipe}, 'scale'],
                'b': ['[b] Back.', {'action':False}, 'login']}
    elif name == 'select':
        return {'1': ['\n[1] Select Recipe.',{'action':select_recipe}, 'scale'],
                'b': ['[b] Back.', {'action':False}, 'login']}
    elif name == 'edit':
         return {'1': ['\n[1] Edit Recipe.',{'action':edit_recipe}, 'edit'],
                 '2': ['[2] Remove recipe.', {'action':delete_recipe}, 'edit'],
                 'b': ['[b] Back.', {'action':False}, 'login']}   
    else:
        return print('\Error, %s not found' % name)


### MAIN PROGRAM ###   
            
os.system('cls')
f = Figlet(font='slant')
print(f.renderText('Recipebook'))
print("\nCreated by Sarah Morris, 2020.")
time.sleep(2)

debug = False
  
users = load_users()

choice = ''
display_title_bar()
menu_location = 'main'
while choice != 'q':    
    # Let users know what they can do.
    menu_select = menus(menu_location)
    for key, value in menu_select.items():
        print(value[0])
    choice = input("What would you like to do? ")
    # Respond to the user's choice.
    display_title_bar()
    if choice == '1':
        var = menu_select['1'][1]['action']()
        if var:
            menu_location = (menu_select['1'][2])
        else:
            menu_location = 'main'
        if debug:
            print(menu_location)
    elif choice == '2':
        menu_select['2'][1]['action']()
        menu_location = (menu_select['2'][2])
    elif choice == 'b':
        if menu_select['b'][1]['action']:
             menu_select['b'][1]['action']()
        menu_location = (menu_select['b'][2])
    elif choice == 'q':
        quit()
    else:
        print("\nI didn't understand that choice.\n")
        
    
    