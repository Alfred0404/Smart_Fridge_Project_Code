import cv2


def calculate_center(x1: int, y1: int, x2: int, y2: int) -> tuple[float, float]:
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2
    return (x_center, y_center)


def is_object_moving_downward(
    center_1: tuple[int, int], center_2: tuple[int, int]
) -> bool:
    return center_1[1] < center_2[1]


def show_center(frame: cv2.Mat, center: tuple[float, float]) -> None:
    """
    Display the center of an object on the given frame.

    @param frame: The frame to display the center on.
    @param center: A tuple containing the x and y coordinates of the center.
    @return: None
    """
    x, y = center
    cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 0), -1)
    cv2.putText(
        frame,
        f"{int(x)},{int(y)}",
        (int(x), int(y)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        1,
    )


def process_frame(frame: cv2.Mat, results: list) -> None:
    """
    Process a frame by drawing the centers of the bounding boxes on the frame.

    Args:
        frame (cv2.Mat): The frame to process.
        results (list): The results of the YOLOv11 detection.
    """
    for result in results:
        for box in result.boxes:
            center = calculate_center(*box.xyxy[0])
            show_center(frame, center)
