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
        print(f"Recipe: {recipe['id']} - {recipe['title']}")
        get_recipe_instructions_by_id(recipe["id"], recipe['title'])


def get_recipe_instructions_by_id(id: int, title: str):
    url = f"https://api.spoonacular.com/recipes/{id}/analyzedInstructions"
    params = {
        "apiKey": os.getenv("SPOONACULAR_API_KEY"),
        "includeNutrition": "false",
    }

    response = r.get(url, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")

    recipe_data = response.json()[0]
    recipe_data["name"] = title
    with open("src/recipes_suggestions/recipes.json", "r+") as f:
        recipes_data = json.load(f)
        recipes_data.append(recipe_data)
        f.seek(0)
        json.dump(recipes_data, f, indent=4)
        f.truncate()

if __name__ == "__main__":
    with open("src/vision/utils/items_in_fridge.json", "r") as f:
        food_list = json.load(f)

    get_recipes_by_ingredients(ingredients=food_list)
