import logging
import os

import cv2
import torch
from ultralytics import YOLO
from utils.detection_utils import *
from utils.video_utils import *

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

# CONSTANTS
WORKING_DIR = os.getcwd()
CONFIDENCE = 0.4
EXIT_KEY = ord("q")


def train_model(model: YOLO, dataset_path: str, epochs: int) -> YOLO:
    """
    Train a YOLO model.

    @return: YOLO model
    """
    model.train(
        data=dataset_path,
        epochs=epochs,
        batch=8,
        imgsz=640,
        device=0,
    )
    return model


def detect_items_in_frame(frame: cv2.Mat, model: YOLO) -> list:
    """
    Detect items in a frame using a YOLO model.

    Args:
        frame (cv2.Mat): The frame to detect items in.
        model (YOLO): The YOLO model to use for detection.

    Returns:
        list: A list of Results objects containing the detected items.
    """
    results = model.track(source=frame, conf=CONFIDENCE, show=False)
    return results


def run_yolov11_detection(model: YOLO) -> None:
    """
    Run YOLOv11 detection on frames from a camera.

    @param model: YOLO model
    @return: None
    """
    logging.info("Starting YOLOv11 detection...")
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        raise RuntimeError("Impossible d'ouvrir la camera")

    try:
        while video_capture.isOpened():
            frame = capture_frame(video_capture)

            results = detect_items_in_frame(frame, model)
            process_frame(frame, results)

            cv2.imshow("YOLOv11 Detection", results[0].plot())

            if cv2.waitKey(1) & 0xFF == EXIT_KEY:
                break

    except Exception as e:
        print(f"[run_yolov11_detection]\tError: {e}")

    finally:
        destroy(video_capture)


if __name__ == "__main__":
    yolo_model_path = os.path.join(WORKING_DIR, "src", "vision", "models", "yolo11n.pt")
    yolo_dataset_path = os.path.join(WORKING_DIR, "src", "vision", "dataset", "data.yaml")
    model = YOLO(yolo_model_path)
    model = train_model(model, yolo_dataset_path, 100)

    run_yolov11_detection(model)
