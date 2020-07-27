# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:19:52 2020

@author: 212488697
"""

class Recipe:
    def __init__(self, title, ingredients, instructions, **kwargs):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __str__(self):
        return '{}'.format(self.title)

class Recipebook:
    def __init__(self, recipes=None):
        self.recipes = recipes
        
    @classmethod    
    def create_cookbook(cls, recipe_list):
        recipes = []
        for title, ingredients, instructions in recipe_list:
            recipes.append(Recipe(title, ingredients, instructions))
        return cls(recipes)
    
    def add_recipe(self, recipe):
        self.recipe = recipe
        for title, ingredients, instructions in recipe:
            self.recipes.append(Recipe(title, ingredients, instructions))

    def __len__(self):
        return len(self.slots)
    
    def __contains__(self, recipe):
        return recipe in self.slots
    
    def __iter__(self):
        yield from self.recipes       
            
class User:
    def __init__(self, name, recipes=None):
        self.name = name
        self.recipes = recipes
        
    @classmethod
    def create_recipebook(cls, recipe_list):
        recipes = []
        for title, ingredients, instructions in recipe_list:
            print(title)
            recipes.append(Recipe(title, ingredients, instructions))
        return cls(recipes)
    
    def add_recipe(self, recipe):
        self.recipe = recipe
        for title, ingredients, instructions in recipe:
            self.recipes.append(Recipe(title, ingredients, instructions))

    def __len__(self):
        return len(self.recipes)
    
    def __contains__(self, recipe):
        return recipe in self.recipes
    
    def __iter__(self):
        yield from self.recipes    
            
    def __str__(self):
        return '{}'.format(self.name)
        
class UserList:
    def __init__(self, users=None):
        self.users = users
        
    @classmethod    
    def create_userlist(cls, user_list):
        users = []
        for name in user_list:
            users.append(User(name))
        return cls(users)
    
    def add_user(self, user):
        self.user = user
        for name in user:
            self.users.append(User(name))

    def __len__(self):
        return len(self.users)
    
    def __contains__(self, users):
        return user in self.users
    
    def __iter__(self):
        yield from self.users
        
        
#new_book = Recipebook.create_cookbook([('Grilled Cheese', '3 cheeses', 'cook'), ('pizza', 'pepperoni', 'bake')])
#
#new_book.add_recipe([('donut', 'flour', 'fry')])
#
#for recipe in new_book:
#    print(recipe)
        
new_user_list = UserList.create_userlist([('Sarah'), ('Devin')])

new_user_list.add_user([('Kitty')])
user_list = []

for user in new_user_list:
    user_list.append(User(user))
    
#user_list[0].add_recipe([('Grilled Cheese', '3 cheeses', 'cook'), ('pizza', 'pepperoni', 'bake')])
#for recipe in user_list[0]:
#    print(recipe)
