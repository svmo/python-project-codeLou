# python-project-codeLou
Repo for my python project for Code Louisville 2020

## Project ideas:
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
