import cv2
from app.Model.Model_cascades import Cascades


class EyesDetection:
    def __init__(self):
        self.type_cascade = Cascades.EYECASCADE

    def get_type_cascade(self):
        return self.type_cascade

    def detection_rectangle_dimensions(self):
        scaleFactor = 1.5
        minNeighbors = 10
        minSize = (5, 5)
        return [scaleFactor, minNeighbors, minSize]

    def format_rectangle(self, image, x, y, w, h):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    def detection_rectangle(self, rectangle: list, x, y, w, h):
        new_rectangle = rectangle[y:y + h, x:x + w]
        return new_rectangle

    def detection_color(self, image):
        color = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return color
