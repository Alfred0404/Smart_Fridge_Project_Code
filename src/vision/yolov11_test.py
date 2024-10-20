from ultralytics import YOLO


def test_yolov11():
    yolo_model_path = "C:\\Users\\ASUS ROG ALFRED\\Documents\\ECE\\ING3\\New York\\Courses\\Intelligent Robotics\\Project_SmartFridge\\Smart_Fridge_Project_Code\\src\\vision\\models\\yolo11n.pt"
    model = YOLO(yolo_model_path)
    results = model.predict(source=0, show=True)

if __name__ == "__main__":
    test_yolov11()
