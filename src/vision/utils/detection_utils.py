import cv2


def calculate_center_of_box(x1: int, y1: int, x2: int, y2: int) -> tuple[float, float]:
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2
    return (x_center, y_center)


def is_object_moving_downward(
    pos_1: tuple[int, int], pos_2: tuple[int, int], frame: cv2.Mat
) -> bool:
    vertical_middle: int = frame.shape[0] // 2
    return True if pos_1[1] > vertical_middle and pos_2[1] < vertical_middle else False


def show_center_of_object(frame: cv2.Mat, center: tuple[float, float]) -> None:
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


def show_horizontal_middle_line(frame: cv2.Mat) -> None:
    """
    Display a line at the horizontal middle of the frame.

    @param frame: The frame to display the center on.
    @return: None
    """
    vertical_middle: int = frame.shape[0] // 2
    cv2.line(
        frame, (0, vertical_middle), (frame.shape[1], vertical_middle), (0, 255, 0), 1
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
            center = calculate_center_of_box(*box.xyxy[0])
            show_center_of_object(frame, center)

    show_horizontal_middle_line(frame)
