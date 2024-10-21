import cv2


def destroy(video_capture: cv2.VideoCapture) -> None:
    video_capture.release()
    cv2.destroyAllWindows()


def capture_frame(video_capture: cv2.VideoCapture) -> cv2.Mat:
    ret, frame = video_capture.read()
    if not ret:
        raise RuntimeError("Erreur lors de la capture de la frame")
    return frame
