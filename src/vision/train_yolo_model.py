import logging
import os

import torch
from ultralytics import YOLO
from utils.config import *

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


def log_training_info() -> None:
    logging.info(f"cuda version: {torch.version.cuda}")
    logging.info(f"gpu used: {torch.cuda.get_device_name(0)}")


def train_model(model: YOLO, dataset_path: str, epochs: int, cuda: bool = True) -> YOLO:
    """
    Train a YOLO model. Returns the trained model.

    @return: YOLO model
    """
    logging.info(f"Starting YOLOv11 training... epochs: {epochs} | cuda: {cuda}")
    log_training_info()

    model.train(
        data=dataset_path,
        epochs=epochs,
        batch=8,
        imgsz=640,
        device=0 if cuda else "cpu",
    )
    return model


if __name__ == "__main__":
    model = YOLO(UNTRAINED_MODEL_PATH)
    model = train_model(model, DATASET_PATH, 100)
