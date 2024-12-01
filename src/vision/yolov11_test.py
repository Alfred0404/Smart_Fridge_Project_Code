import sys

sys.path.append("src/vision")

import logging

import cv2
from ultralytics import YOLO
from utils.config import *
from utils.detection_utils import *
from utils.video_utils import *
from utils.yolo_utils import *
from utils.list_update_utils import *

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


def detect_items_in_frame(frame: cv2.Mat, model: YOLO) -> list:
    """
    Detect items in a frame using a YOLO model.

    Args:
        frame (cv2.Mat): The frame to detect items in.
        model (YOLO): The YOLO model to use for detection.

    Returns:
        list: A list of Results objects containing the detected items.
    """
    items_detected = model.track(source=frame, conf=CONFIDENCE, show=False)
    return items_detected


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

            items_detected = detect_items_in_frame(frame, model)
            center_history = process_frame(frame, items_detected)
            print("updating fridge items...")

            try:
                update_fridge_items(frame, items_detected, center_history)
            except json.JSONDecodeError as e:
                print(f"[run_yolov11_detection]\tError: {e}")

            cv2.imshow("YOLOv11 Detection", items_detected[0].plot())

            key = cv2.waitKey(1) & 0xFF
            if key == EXIT_KEY or key == ord("q"):
                break

    except Exception as e:
        print(f"[run_yolov11_detection]\tError: {e}")

    finally:
        destroy(video_capture)


if __name__ == "__main__":
    model = get_model()
    run_yolov11_detection(model)


"""
items to train the model on:
- milk
- vegetables (tomatoes, epinards, carrots, onions, lettuce, etc.)
- sauces (mayonnaise, bbq, etc.)
- sausages
"""
