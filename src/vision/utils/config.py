import os

# CONSTANTS
CONFIDENCE = 0.5
EXIT_KEY = ord("q")

# PATHS
WORKING_DIR = os.getcwd()
TRAINED_MODEL_PATH = os.path.join(
    WORKING_DIR, "runs", "detect", "train", "weights", "best.pt"
)
UNTRAINED_MODEL_PATH = os.path.join(
    WORKING_DIR, "src", "vision", "models", "yolo11n.pt"
)

DATASET_PATH = os.path.join(WORKING_DIR, "src", "vision", "fridge_dataset", "data.yaml")
