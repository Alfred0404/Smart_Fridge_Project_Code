from vision.utils.config import *
from vision.utils.detection_utils import *
from vision.utils.video_utils import *
from vision.utils.yolo_utils import *
from vision.utils.list_update_utils import *


# Maintenant, vous pouvez importer les modules correctement
from vision.yolov11_test import run_yolov11_detection
from recipes_suggestions.spoonacular_api_test import get_recipes_by_ingredients

if __name__ == "__main__":
    model = get_model()
    run_yolov11_detection(model)
    print("finito capturer")

    with open("src/vision/utils/items_in_fridge.json", "r") as f:
        food_list = json.load(f)
    get_recipes_by_ingredients(ingredients=food_list)
