import logging

import cv2
from ultralytics import YOLO
from utils.config import *
from utils.detection_utils import *
from utils.video_utils import *
from utils.yolo_utils import *

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
    model = get_model()
    run_yolov11_detection(model)
