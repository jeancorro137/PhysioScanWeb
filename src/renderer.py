import cv2
import mediapipe as mp


class PoseRenderer:
    """
    Encargado del renderizado visual del esqueleto
    y overlays gráficos.
    """

    def __init__(self):

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose

    def draw_pose(self, frame, results):
        """
        Dibuja el esqueleto sobre el frame.
        """

        if results.pose_landmarks:

            self.mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS,
            )

        return frame

    def draw_angle(self, frame, text, x, y):
        """
        Dibuja un texto sobre el frame.
        """

        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

        return frame