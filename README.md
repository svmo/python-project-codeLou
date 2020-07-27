# Recipebook
Repo for my python project for Code Louisville 2020

## What is it
This program allows users to create their own cookbook. Once you have a login name, the program will allow the user to import recipes using a URL.

Note: Recipe scaling has not been implemented in this release.

## Technical Summary
* Python

## Requirements
The following libraries must be installed to use this repo:
* [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
    * pip install pyfiglet
* [recipe_scrapers](https://github.com/hhursev/recipe-scrapers) 
    * pip install recipe-scrapers
* os
* time
* json

The program can be run by cloning the repo. Once downloaded, navigate to the folder containing the recipe-app.py. The program runs in the terminal, simply run python recipe-app.py. Follow the menu prompts to login or create a new user. To import a recipe, follow the prompts and then paste in the URL for the recipe you would like to save. Most major recipe websties are supported, see the [recipe_scrapers](https://github.com/hhursev/recipe-scrapers) repo for more information. The recipe_app_data file is where all the user and recipe information is stored. 

## Features
* "Master loop" console app, user can enter commands and exit
* A dictionary that stores the user information like the name and recipes
* The program reads and writes to an external text file
* The program pulls from an external API (recipe_scraper) that scrapes the recipe information from a valid URL
* Functions:
   * login() function displays the login information when selected from the menu
   * add_new_recipe() function asks for a URL and then displays the recipe
   * show_recipe_list() shows all recipes a user has saved and lets the user select one
   * scale_recipe() has not been implemented but would allow the user to scale a given recipe

## Future project ideas:
* Command line recipe program that will auto half a recipe
  * master loop app
  * conversion app
  * read from external file or API: [recipe scraper](https://github.com/hhursev/recipe-scrapers/)
  * MVP
    * UI that let's users input a URL and scale factor
    * regex ot verify website
    * function to pass URL to API and extract recipe
    * save recipe into a dict
    * convert recipe to whatever scaled amount (just decimals)
    * print out resulting scaled recipe 
    * recipe class:
        * attributes: name, ingredients, rating, time, difficulty, special diets, instructions
        * methods: save recipe to file, scale recipe
