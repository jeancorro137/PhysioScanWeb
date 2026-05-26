import cv2
import mediapipe as mp

from src.pose_detector import PoseDetector
from src.renderer import PoseRenderer
from src.geometry import calculate_angle
from collections import deque


class VideoProcessor:
    """
    Pipeline principal del motor de visión.
    """

    def __init__(self):

        self.detector = PoseDetector()
        self.renderer = PoseRenderer()
        self.mp_pose = mp.solutions.pose

        self.cap = cv2.VideoCapture(0)

        # Buffers Moving Average
        self.left_shoulder_buffer = deque(maxlen=5)
        self.right_shoulder_buffer = deque(maxlen=5)
        self.head_buffer = deque(maxlen=5)
        self.cervical_buffer = deque(maxlen=5)

    def process_frame(self):

        success, frame = self.cap.read()

        if not success:
            return None, None

        # Detectar pose
        results = self.detector.detect_pose(frame)

        # Diccionario de métricas
        metrics = {
            "cervical": None,
            "left_shoulder": None,
            "right_shoulder": None,
            "head": None
        }

        # Calcular ángulos si hay landmarks
        if results.pose_landmarks:

            landmarks = results.pose_landmarks.landmark

            h, w, _ = frame.shape

            # =========================
            # HOMBRO IZQUIERDO
            # =========================
            left_shoulder = landmarks[
                self.mp_pose.PoseLandmark.LEFT_SHOULDER.value
            ]

            left_elbow = landmarks[
                self.mp_pose.PoseLandmark.LEFT_ELBOW.value
            ]

            left_hip = landmarks[
                self.mp_pose.PoseLandmark.LEFT_HIP.value
            ]

            left_shoulder_angle = calculate_angle(
                [
                    left_elbow.x,
                    left_elbow.y,
                    left_elbow.z
                ],
                [
                    left_shoulder.x,
                    left_shoulder.y,
                    left_shoulder.z
                ],
                [
                    left_hip.x,
                    left_hip.y,
                    left_hip.z
                ]
            )

            self.left_shoulder_buffer.append(
                left_shoulder_angle
            )

            left_shoulder_angle = sum(
                self.left_shoulder_buffer
            ) / len(self.left_shoulder_buffer)

            metrics["left_shoulder"] = int(
            left_shoulder_angle
            )

            x_l = int(left_shoulder.x * w)
            y_l = int(left_shoulder.y * h)

            frame = self.renderer.draw_angle(
                frame,
                f"{int(left_shoulder_angle)} hombro",
                x_l,
                y_l
            )

            # =========================
            # HOMBRO DERECHO
            # =========================
            right_shoulder = landmarks[
                self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value
            ]

            right_elbow = landmarks[
                self.mp_pose.PoseLandmark.RIGHT_ELBOW.value
            ]

            right_hip = landmarks[
                self.mp_pose.PoseLandmark.RIGHT_HIP.value
            ]

            right_shoulder_angle = calculate_angle(
                [
                    right_elbow.x,
                    right_elbow.y,
                    right_elbow.z
                ],
                [
                    right_shoulder.x,
                    right_shoulder.y,
                    right_shoulder.z
                ],
                [
                    right_hip.x,
                    right_hip.y,
                    right_hip.z
                ]
            )

            self.right_shoulder_buffer.append(
                right_shoulder_angle
            )

            right_shoulder_angle = sum(
                self.right_shoulder_buffer
            ) / len(self.right_shoulder_buffer)

            metrics["right_shoulder"] = int(
            right_shoulder_angle
            )

            x_r = int(right_shoulder.x * w)
            y_r = int(right_shoulder.y * h)

            frame = self.renderer.draw_angle(
                frame,
                f"{int(right_shoulder_angle)} hombro",
                x_r,
                y_r
            )

            # =========================
            # CABEZA-HOMBROS
            # =========================
            nose = landmarks[
                self.mp_pose.PoseLandmark.NOSE.value
            ]

            head_shoulders_angle = calculate_angle(
                [
                    left_shoulder.x,
                    left_shoulder.y,
                    left_shoulder.z
                ],
                [
                    nose.x,
                    nose.y,
                    nose.z
                ],
                [
                    right_shoulder.x,
                    right_shoulder.y,
                    right_shoulder.z
                ]
            )

            self.head_buffer.append(
                head_shoulders_angle
            )

            head_shoulders_angle = sum(
                self.head_buffer
            ) / len(self.head_buffer)

            metrics["head"] = int(
                head_shoulders_angle
            )

            x_n = int(nose.x * w)
            y_n = int(nose.y * h)

            frame = self.renderer.draw_angle(
                frame,
                f"{int(head_shoulders_angle)} cabeza",
                x_n,
                y_n
            )

            # =========================
            # CERVICAL CLINICA
            # Oreja-Hombro-Cadera
            # =========================
            left_ear = landmarks[
                self.mp_pose.PoseLandmark.LEFT_EAR.value
            ]

            cervical_angle = calculate_angle(
                [
                    left_ear.x,
                    left_ear.y,
                    left_ear.z
                ],
                [
                    left_shoulder.x,
                    left_shoulder.y,
                    left_shoulder.z
                ],
                [
                    left_hip.x,
                    left_hip.y,
                    left_hip.z
                ]
            )

            self.cervical_buffer.append(
                cervical_angle
            )

            cervical_angle = sum(
                self.cervical_buffer
            ) / len(self.cervical_buffer)

            metrics["cervical"] = int(
                cervical_angle
            )

            x_c = int(left_ear.x * w)
            y_c = int(left_ear.y * h) - 40

            frame = self.renderer.draw_angle(
                frame,
                f"{int(cervical_angle)} cervical",
                x_c,
                y_c
            )

        # Dibujar pose
        frame = self.renderer.draw_pose(
            frame,
            results
        )

        return frame, metrics

    def release(self):

        self.cap.release()
        self.detector.close()

        cv2.destroyAllWindows()