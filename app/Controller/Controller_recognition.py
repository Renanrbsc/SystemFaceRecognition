import cv2
from app.Model.Model_cascades import Cascades
from app.Model.Model_screen import Screen


class ControllerRecognition:
    def __init__(self, platform):
        self.screen = Screen(platform)

    def face_detection_cascade(self):
        cascade = Cascades(Cascades.FACECASCADE)
        self.screen.set_dimension()

        while True:
            image = self.screen.read()
            self.screen.redimension_image()
            color = self.screen.detection_color()
            recognition = cascade.detect_multi_scale(color)

            for (x, y, w, h) in recognition:
                self.screen.format_rectangle(x, y, w, h)
                self.screen.detection_rectangle(color, x, y, w, h)
                self.screen.detection_rectangle(image, x, y, w, h)

            self.screen.title_screen()

            if self.screen.close_screen():
                break

        self.screen.release()
        self.screen.close_all_windows()
