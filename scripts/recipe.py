# pylint: disable=missing-docstring,line-too-long
#from pydoc import source_synopsis
#from re import search
import sys
from os import path
import csv
from bs4 import BeautifulSoup
import requests


def parse(html):
    ''' return a list of dict {name, difficulty, prep_time} '''
    #response = requests.get(html)
    soup = BeautifulSoup(html, "html.parser")
    recipe_list = []
    for recipe in soup.find_all('div', class_= 'col-12 col-sm-6 col-md-4 col-lg-3'):
        name =recipe.find("p", class_ = "text-dark text-truncate w-100 font-weight-bold mb-0 recipe-name").string
        difficulty = recipe.find("span", class_ = "recipe-difficulty").string
        prep_time = recipe.find("span", class_ = "recipe-cooktime").string
        recipe_list.append({'name':name, 'difficulty': difficulty,'prep_time':prep_time})
    #print(type(recipe_list))
    return recipe_list

    #pass  # YOUR CODE HERE

def parse_recipe(article):
    ''' return a dict {name, difficulty, prep_time} modelising a recipe'''
    pass  # YOUR CODE HERE

def write_csv(ingredient, recipes):
    ''' dump recipes to a CSV file `recipes/INGREDIENT.csv` '''
    keys = recipes[0].keys()
    with open(f'recipes/{ingredient}.csv', 'w', newline='',encoding="utf8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(recipes)
    # YOUR CODE HERE

def scrape_from_internet(ingredient): #start=1):
    ''' Use `requests` to get the HTML page of search results for given ingredients. '''
    url = f'https://recipes.lewagon.com/?search[query]={ingredient}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    htmls = f'pages/{ingredient}.html'
    with open(htmls, 'w', encoding="utf8") as html_file:
        html_file.write(str(soup))

    return htmls
    #pass  # YOUR CODE HERE

def scrape_from_file(ingredient):
    file = f"pages/{ingredient}.html"
    if path.exists(file):
        return open(file, encoding="utf8")
    print("Please, run the following command first:")
    print(f'curl "https://recipes.lewagon.com/?search[query]={ingredient}" > pages/{ingredient}.html')
    sys.exit(1)


def main():
    if len(sys.argv) > 1:
        ingredient = sys.argv[1]
        #Replace scrape_from_file with scrape_from_internet and implement pagination (more than 2 pages needed)
        recipes = parse(scrape_from_internet(ingredient))
        write_csv(ingredient, recipes)
        # YOUR CODE HERE
    else:
        print('Usage: python recipe.py INGREDIENT')
        sys.exit(0)


if __name__ == '__main__':
    main()
