import cv2


class Cascades:
    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
    FACECASCADE = 'app/Model/Cascades/haarcascade_frontalface_default.xml'
    EYECASCADE = 'app/Model/Cascades/haarcascade_eye.xml'
    SMILECASCADE = 'app/Model/Cascades/haarcascade_smile.xml'

    def __init__(self, type_cascade):
        self.cascade = cv2.CascadeClassifier(type_cascade)

    def detect_multi_scale(self, color, dimensions: list):
        cascade = self.cascade.detectMultiScale(color,
                                                scaleFactor=dimensions[0],
                                                minNeighbors=dimensions[1],
                                                minSize=dimensions[2]
                                                )
        return cascade
