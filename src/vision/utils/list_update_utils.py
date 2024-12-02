import json


def read_json_file(file_path: str):
    with open(file_path, "r") as f:
        json_object = json.load(f)
    return json_object


def update_fridge_items(detections: list) -> None:
    """
    Update the contents of the fridge based on the unique detections.
    Args:
        detections (list): A list of Results objects from the YOLOv11 model.
    """
    try:
        with open("src/vision/utils/items_in_fridge.json", "r") as file:
            fridge_items = set(json.load(file))
    except FileNotFoundError:
        print(
            "[update_fridge_items]\tFridge items file not found. Creating a new one..."
        )
        fridge_items = set()

    for detection in detections:
        for box in detection.boxes:
            item_name = detection.names[box.cls.item()]
            fridge_items.add(item_name)

    with open("src/vision/utils/items_in_fridge.json", "w") as file:
        json.dump(list(fridge_items), file)
