import json


def read_json_file(file_path: str):
    with open(file_path, "r") as f:
        json_object = json.load(f)
    return json_object


def update_fridge_items(detections: list) -> None:
    """
    Update the contents of the fridge based on the latest detections.

    Args:
        detections (list): A list of Results objects from the YOLOv11 model.
    """
    try:
        with open("src/vision/utils/items_in_fridge.json", "r") as file:
            fridge_items = json.load(file)
    except FileNotFoundError:
        fridge_items = {}

    for detection in detections:
        for box in detection.boxes:
            item_name = detection.names[box.cls.item()]
            fridge_items[item_name] = fridge_items.get(item_name, 0) + 1

    print(f"[update_fridge_items]\tUpdated fridge items: {fridge_items}")

    with open("src/vision/utils/items_in_fridge.json", "w") as file:
        json.dump(fridge_items, file)
