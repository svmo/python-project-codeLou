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
import json

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
   if login_user in user_info.keys():
       print("\nWelcome back %s!" % login_user)
       return login_user
   if login_user not in key:
       print("Sorry, I don't recognize that name. Please return to the main menu.")
        
def get_new_user():
     # Asks the user for a new name, and stores the name if we don't already
    #  know about this person.
    new_user = input("\nPlease enter your name: ")
    if new_user in user_info.keys():
        print("\n%s is already a user. Please login" % new_user.title())
    else:
        user_info[new_user] = []
        if debug:
            print(user_info)
        print("\nWelcome to the kitchen, %s!\n" % new_user.title())
    
def load_users():
    # This function loads names from a file, and puts them in the list 'names'.
    #  If the file doesn't exist, it creates an empty list.
    try:
        with open('recipe_app_data.txt') as json_file:
            names = json.load(json_file)
        print(names)
        return names
    except Exception as e:
        print(e)
        return {}

def add_new_recipe():
    URL = input('What is the recipe URL? ')
    scraper = scrape_me(URL)
    display_title_bar()
    ingredients = []
    print('\n**' + scraper.title()+'**\n')
    print('INGREDIENTS')
    for ingredient in scraper.ingredients():
        ingredients.append(ingredient)
        print(ingredient)
    print('\nINSTRUCTIONS')
#    for instructions in scraper.instructions():
    print(scraper.instructions())
    recipe = {'title':scraper.title(),'ingredients':ingredients, 'instructions':scraper.instructions()}
    if debug:
        print(recipe.title)
    choice = input('Would you like to save this recipe? (y/n) ')
    if choice == 'y':
        save_recipe(recipe)
    return True
    
def save_recipe(recipe):
    print('Recipe ' + recipe['title'] + ' saved succesfully!')
    user_info[current_user].append(recipe)
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
        with open('recipe_app_data.txt', 'w') as outfile:
            json.dump(user_info, outfile)
            print("\nHappy eating! Bye.")
    except Exception as e:
        print("\nUh oh looks like there's a fire in the kitchen.")
        print(e)
        
### CLASSES ###

class Recipe:
    def __init__(self, name, ingredients, instructions, **kwargs):
        self.name = name
        self.ingredients = ingredients
        self.instructions = ingredients
        
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

user_info = load_users()
#users = []
#
#for key, value in user_info.items():
#    users.append(key)

choice = ''
current_user = ''
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
            if menu_location == 'main':
                current_user = var
                if debug:
                    print(current_user)
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
        quits()
    else:
        print("\nI didn't understand that choice.\n")
        
    
    