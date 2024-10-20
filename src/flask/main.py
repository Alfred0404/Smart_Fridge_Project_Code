import sys
import os

# Ajoute dynamiquement le chemin du dossier parent 'src/' au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print(sys.path)

from recipes_suggestions.ingredient import *
from recipes_suggestions.handle_ollama_interactions import *


if __name__ == "__main__":
    food_list = [
        Ingredient("chocolate", "200", "g"),
        Ingredient("banana", "2"),
        Ingredient("apple", "3"),
        Ingredient("fish", "500", "g"),
        Ingredient("pear", "2"),
        Ingredient("steak", "300", "g"),
        Ingredient("pastas", "200", "g"),
        Ingredient("chicken", "400", "g"),
        Ingredient("eggs", "4"),
        Ingredient("ham", "200", "g"),
        Ingredient("mushroom", "150", "g"),
        Ingredient("onion", "1"),
        Ingredient("carrot", "1"),
    ]
    print(get_recipes(ingredients=food_list, limit=3))
