import os
from ultralytics import YOLO
from .config import *


def get_model() -> YOLO:
    """
    Checks if a trained model exists and returns it.
    If not, returns the untrained model.

    @return: YOLO model
    """
    if os.path.exists(TRAINED_MODEL_PATH):
        return YOLO(TRAINED_MODEL_PATH)

    return YOLO(UNTRAINED_MODEL_PATH)
