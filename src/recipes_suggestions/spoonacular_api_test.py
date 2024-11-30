import requests as r
import os
import json
from dotenv import load_dotenv

load_dotenv()


def get_recipes_by_ingredients(ingredients=[], limit=5):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "apiKey": os.getenv("SPOONACULAR_API_KEY"),
        "ingredients": ",".join(ingredients),
        "number": limit,
        "ignorePantry": "true",
        "ranking": 2,
    }

    response = r.get(url, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")

    for recipe in response.json():
        print(f"Recipe: {recipe['id']}- {recipe['title']}")
        get_recipe_instructions_by_id(recipe["id"])


def get_recipe_instructions_by_id(id):
    url = f"https://api.spoonacular.com/recipes/{id}/analyzedInstructions"
    params = {
        "apiKey": os.getenv("SPOONACULAR_API_KEY"),
        "includeNutrition": "false",
    }

    response = r.get(url, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")

    with open("src/recipes_suggestions/recipes.json", "w") as f:
        f.write(response.text)

with open("src/vision/utils/items_in_fridge.json", "r") as f:
    food_list = json.load(f)

get_recipes_by_ingredients(ingredients=food_list)
