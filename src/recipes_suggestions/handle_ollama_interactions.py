import json
import ollama
from recipes_suggestions.ingredient import Ingredient


def clean_response(response):
    """
    Given a string response from the ollama API, strip out the JSON block and decode it.

    Returns:
        str: The decoded JSON string, or None if there was an error parsing the JSON.
    """
    try:
        cleaned_response = (
            response.replace("```json", "").replace("```", "").replace("'", '"').strip()
        )
        print(f"[clean_response]\tcleaned response: {cleaned_response}")

        return cleaned_response

    except (IndexError, json.JSONDecodeError) as e:
        print(f"[clean_response]\tError cleaning response: {e}")

        return None


def response_to_json(response):
    """
    Takes a response from the ollama API and tries to parse it into a list of
    Ingredient objects.

    Args:
        response (str): The response from the ollama API

    Returns:
        list[dict]: A list of Ingredient objects, or None if the response could
        not be parsed
    """
    cleaned_response = clean_response(response)
    if cleaned_response:
        try:
            return json.loads(cleaned_response)

        except json.JSONDecodeError as e:
            print(f"[response_to_json]\tError parsing JSON: {e}")

            return None
    else:
        return None


def get_recipes(ingredients=[], limit=5):
    """
    Given a list of Ingredient objects, query the ollama API to generate a list of 5 recipes based on the ingredients.

    Args:
        ingredients (list[Ingredient]): a list of Ingredient objects

    Returns:
        list[dict]: a list of recipes, each containing a "recipe_name", "ingredients", and "instructions" field.
    """

    print("[get_recipes]\t", [str(ingredient) for ingredient in ingredients])

    food_list_str = [ingredient.to_dict() for ingredient in ingredients]
    example = [
        {
            "recipe_name": "name of the recipe",
            "ingredients": [
                {
                    "ingredient": "ingredient name",
                    "amount": "ingredient amount or unit (e.g., 200g, 2 cups)",
                },
                ...,
            ],
            "instructions": [
                "instruction 1",
                "instruction 2",
                "instruction 3",
                ...,
            ],
        },
        ...,
    ]
    print("[get_recipes]\tfetching recipes...")

    try:
        response = ollama.chat(
            model="hf.co/bartowski/Ministral-8B-Instruct-2410-HF-GGUF-TEST:latest",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    You are a recipe generator. Generate exactly {limit} recipes based on this food list: {food_list_str}.
                    Make sure the response is a valid JSON and that all property names and strings use double quotes only.
                    Do not forget any commas, quotes, or other special characters that might be needed.
                    Generate only one JSON object.
                    Follow this format strictly:
                    ```json
                    {example}
                    ```
                    Each ingredient should include a specific quantity (like "200g", "2 cups", etc.), and the instructions should be clear and concise.
                    Ensure the JSON is syntactically correct, with commas between all key-value pairs.
                    Do not say anything else except for the JSON object.
                    """,
                },
            ],
            stream=False,
        )["message"]["content"]

        print("[get_recipes]\tresponse:", response)
        recipes = response_to_json(response)

        return recipes

    except Exception as e:
        print(f"Error: {e}")


def main():
    ingredients = [
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
    ]

    get_recipes(ingredients)


if __name__ == "__main__":
    main()
