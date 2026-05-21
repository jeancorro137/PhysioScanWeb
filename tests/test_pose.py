import cv2

from src.pose_detector import PoseDetector
from src.renderer import PoseRenderer


def main():

    detector = PoseDetector()
    renderer = PoseRenderer()

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = detector.detect_pose(frame)

        frame = renderer.draw_pose(frame, results)

        cv2.imshow("PhysioScan Web", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    cap.release()
    detector.close()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()