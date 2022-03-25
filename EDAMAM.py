from operator import concat
import requests
import json
#cuisine and health labels
ingredient = str(input('What ingredient did you want? '))
health_label = str(input('What health label are you after? '))
cuisine = str(input('What cuisine would you like? '))

parameters = {
    'health': [
        health_label
    ],
    'cuisineType': [
        cuisine
    ]
}

response = requests.get("https://api.edamam.com/search?q="+ingredient+"&app_id=4df9cb5d&app_key=0236bf0fc36869a5bd9e0a98fae15e1f", params = parameters)

data = response.json()
recipe_amount = data['count']

#output - recipe link, title
for i in range(recipe_amount):
    recipe_name = data['hits'][i]['recipe']['label']
    recipe_link = data['hits'][i]['recipe']['url']
    print(i, recipe_name, recipe_link +'/n')