from ultralytics import YOLO
import cv2
import os


def calculate_center(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


def is_moving_forward(center_1, center_2):
    # check if an item is moving forward (from top to bottom)
    _, y1 = center_1
    _, y2 = center_2

    return True if y1 < y2 else False


def destroy(cap):
    cap.release()
    cv2.destroyAllWindows()


def test_yolov11(model):
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, conf=0.4, show=False)

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x_center, y_center = calculate_center(x1, y1, x2, y2)
                cv2.circle(frame, (int(x_center), int(y_center)), 3, (0, 255, 0), -1)
                cv2.putText(
                    frame,
                    f"{int(x_center)},{int(y_center)}",
                    (int(x_center), int(y_center)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1,
                )

        cv2.imshow("YOLOv11 Detection", results[0].plot())

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    destroy(cap)


if __name__ == "__main__":
    working_dir = os.getcwd().replace("\\", "\\\\")
    yolo_model_path = f"{working_dir}\\src\\vision\\models\\yolo11n.pt"
    model = YOLO(yolo_model_path)
    test_yolov11(model)
