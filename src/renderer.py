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