import cv2
import mediapipe as mp


class PoseDetector:
    """
    Detector de pose utilizando MediaPipe BlazePose.
    """

    def __init__(
        self,
        static_image_mode=False,
        model_complexity=1,
        smooth_landmarks=True,
        enable_segmentation=False,
        smooth_segmentation=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ):

        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils

        self.pose = self.mp_pose.Pose(
            static_image_mode=static_image_mode,
            model_complexity=model_complexity,
            smooth_landmarks=smooth_landmarks,
            enable_segmentation=enable_segmentation,
            smooth_segmentation=smooth_segmentation,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def detect_pose(self, frame):
        """
        Procesa un frame y detecta landmarks corporales.
        """

        # Convertir BGR -> RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Optimización de memoria
        rgb_frame.flags.writeable = False

        # Procesamiento BlazePose
        results = self.pose.process(rgb_frame)

        # Restaurar escritura
        rgb_frame.flags.writeable = True

        return results

    def close(self):
        """
        Libera recursos de MediaPipe.
        """
        self.pose.close()