from app.Model.Model_cascades import Cascades
from app.Model.Model_facedetection import FaceDetection
from app.Model.Model_eyesdetection import EyesDetection
from app.Model.Model_screen import Screen


class ControllerRecognition:
    def __init__(self, platform):
        self.screen = Screen(platform)
        self.face = FaceDetection()
        self.eyes = EyesDetection()

    def face_detection_cascade(self):
        type_face = self.face.get_type_cascade()
        type_eyes = self.eyes.get_type_cascade()
        face_cascade = Cascades(type_face)
        eyes_cascade = Cascades(type_eyes)
        self.screen.set_dimension()

        while True:
            self.screen.read()
            image = self.screen.redimension_image()
            color = self.face.detection_color(image)
            face_dimensions = self.face.detection_rectangle_dimensions()
            face_recognition = face_cascade.detect_multi_scale(color, face_dimensions)

            for (x, y, w, h) in face_recognition:
                self.face.format_rectangle(image, x, y, w, h)
                color = self.face.detection_rectangle(color, x, y, w, h)
                image = self.face.detection_rectangle(image, x, y, w, h)

                eyes_dimensions = self.eyes.detection_rectangle_dimensions()
                eyes_recognition = eyes_cascade.detect_multi_scale(color, eyes_dimensions)

                for (a, b, c, d) in eyes_recognition:
                    self.eyes.format_rectangle(image, a, b, c, d)

            self.screen.title_screen()

            if self.screen.close_screen():
                break

        self.screen.release()
        self.screen.close_all_windows()
