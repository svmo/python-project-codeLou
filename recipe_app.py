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
from pyfiglet import Figlet
import time
from recipe_scrapers import scrape_me
import json

'''
TODO

+ scale recipes
    [] regex for getting numbers
    [] how to pass in recipe
[] regex for url
[] regex for user name
[] delete recipes

'''

### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('cls')
              
    print("\t*********************************************")
    print("\t***  Recipebook - Hello hungry friends!  ***")
    print("\t*********************************************")
    
def login():
    #  asks for login information
   login_user = input("\nPlease enter your name: ").capitalize()
   display_title_bar()
   if login_user in user_info.keys():
       print("\nWelcome back %s!" % login_user)
       return login_user
   if login_user not in key:
       print("Sorry, I don't recognize that name. Please return to the main menu.")
        
def get_new_user():
     # Asks the user for a new name, and stores the name if we don't already
    #  know about this person.
    new_user = input("\nPlease enter your name: ").capitalize()
    if new_user in user_info.keys():
        print("\n%s is already a user. Please login" % new_user.title())
    else:
        user_info[new_user] = []
        if debug:
            print(user_info)
        display_title_bar()
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
    #  this function adds new recipes via a URL and displays the recipe
    print("Try this URL if you need inspiration: https://www.allrecipes.com/recipe/8499/basic-chicken-salad\n")
    URL = input('What is the recipe URL? ')
    try:
        scraper = scrape_me(URL)
        display_title_bar()
        ingredients = []
        print('\n**' + scraper.title()+'**\n')
        print("Yields: {}\n".format(scraper.yields()))
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
        choice = input('\nWould you like to save this recipe? (y/n) ')
        if choice == 'y':
            save_recipe(recipe)
        display_title_bar()
        return True
    except:
        print("That website is not supported, please try again.")
        return True

def display_recipe(recipe):
    #  this function displays the recipe
    display_title_bar()
    title = recipe['title']
    print('\n**' + title+'**\n')
    print('INGREDIENTS')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('\nINSTRUCTIONS')
    print(recipe['instructions'])
    
def save_recipe(recipe):
    # this function saves the recipe
    print('\nRecipe ' + recipe['title'] + ' saved succesfully!')
    user_info[current_user].append(recipe)
    return recipe
    
def scale_recipe(recipe):
    display_title_bar()
    print('\n[1] Half the recipe')
    print('[2] Double the recipe')

    choice = input('How would you like to scale the recipe? ')
    if choice == '1':
        print(recipe['title'] + ' scaled by half')
    if choice == '2':
        print(recipe['title'] + ' doubled')
    display_title_bar()
    print('This is where a user will be able to scale a recipe')
    return True
    
def edit_recipe():
    print('A user will be able to edit their recipe, maybe')
    return True
    
def delete_recipe():
    display_title_bar()
    print('Delete recipes here')
    return True
    
def show_recipe_list():
    # this function shows the list of recipes a user has saved
    if debug:
        print('Show what recipes a user has, maybe select recipe too')
    for idx, value in enumerate(user_info[current_user]):
        print('[{}] {}'.format(idx+1, value['title']))
    if len(user_info[current_user]) > 0:
        choice = input('Please select a recipe: ')
        if int(choice) <= len(user_info[current_user]):
            recipe = user_info[current_user][int(choice) - 1]
            display_recipe(user_info[current_user][int(choice) - 1])
        else:
            print('That is not a valid selection.')
        print('\n[1] Delete Recipe.')
        print('[b] Back.')
        print('[q] Quit.')
        choice = input("What would you like to do? ")
        if choice == '1':
            delete_recipe()
        elif choice == 'b':
            display_title_bar()
            return recipe
    else:
        print("Please add a recipe first.")
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
        
def menus(name):
    if name == 'login':
        return {'1': ['\n[1] Login.', {'action':login}, 'main'],
                '2': ['[2] New user.', {'action':get_new_user}, 'login'],
                'q': ['[q] Quit.', {'action':quits}]}
    elif name == 'main':
         return {'1': ['\n[1] New Recipe.', {'action':add_new_recipe}, 'main'],
                 '2': ['[2] View Recipes.',{'action':show_recipe_list}, 'main'],
                 'q': ['[q] Quit.', {'action':quits}]}
    elif name == 'scale':
        return {'1': ['\n[1] Delete Recipe.',{'action':delete_recipe}, 'main'],
                'b': ['[b] Back.', {'action':False}, 'main'],
                'q': ['[q] Quit.', {'action':quits}]}
    elif name == 'edit':
         return {'1': ['\n[1] Edit Recipe.',{'action':edit_recipe}, 'edit'],
                 '2': ['[2] Remove recipe.', {'action':delete_recipe}, 'edit'],
                 'b': ['[b] Back.', {'action':False}, 'login'],
                 'q': ['[q] Quit.', {'action':quits}]}   
    else:
        return print('\Error, %s not found' % name)
        
### CLASSES ###

# this class is unused
        
class Recipe:
    def __init__(self, name, ingredients, instructions, **kwargs):
        self.name = name
        self.ingredients = ingredients
        self.instructions = ingredients
        
        for key, value in kwargs.items():
            setattr(self, key, value)

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
menu_location = 'login'
current_recipe = ''
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
            if menu_location == 'login':
                current_user = var
                if debug:
                    print(current_user)
#            elif menu_location == 'login' or menu_location == 'scale' or menu_location == 'select':
#                current_recipe = var
#                if debug:
#                    print(current_recipe)
            menu_location = (menu_select['1'][2])
        else:
            menu_location = 'login'
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
        
    
    