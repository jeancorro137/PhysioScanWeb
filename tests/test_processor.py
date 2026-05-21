import cv2

from src.processor import VideoProcessor


def main():

    processor = VideoProcessor()

    while True:

        frame = processor.process_frame()

        if frame is None:
            break

        cv2.imshow("PhysioScan Processor", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    processor.release()


if __name__ == "__main__":
    main()