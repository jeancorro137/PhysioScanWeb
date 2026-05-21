import cv2

from src.pose_detector import PoseDetector
from src.renderer import PoseRenderer


class VideoProcessor:
    """
    Pipeline principal del motor de visión.
    """

    def __init__(self):

        self.detector = PoseDetector()
        self.renderer = PoseRenderer()

        self.cap = cv2.VideoCapture(0)

    def process_frame(self):

        success, frame = self.cap.read()

        if not success:
            return None

        # Detectar pose
        results = self.detector.detect_pose(frame)

        # Dibujar pose
        frame = self.renderer.draw_pose(frame, results)

        return frame

    def release(self):

        self.cap.release()
        self.detector.close()

        cv2.destroyAllWindows()