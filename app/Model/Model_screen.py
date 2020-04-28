import cv2


class Screen:
    def __init__(self, platform):
        self.video_capture = cv2.VideoCapture(platform)
        self.image = list()

    def set_dimension(self):
        self.video_capture.set(3, 640)  # set Width
        self.video_capture.set(4, 480)  # set Height

    def read(self):
        retval, self.image = self.video_capture.read()
        return self.image

    def redimension_image(self):
        self.image = cv2.flip(self.image, 0)  # Flip vertically
        self.image = cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)  # Rotate vertically

    def detection_color(self):
        color = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return color

    def title_screen(self):
        cv2.imshow('Facial Recognition System', self.image)

    def format_rectangle(self, x, y, w, h):
        cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    def detection_rectangle(self, rectangle: list, x, y, w, h):
        new_rectangle = rectangle[y:y + h, x:x + w]
        return new_rectangle

    def close_screen(self):
        if cv2.waitKey(30) == 27:
            if input("press 'Q' to quit: ") == 'Q':
                return True
        return False

    def release(self):
        self.video_capture.release()

    def close_all_windows(self):
        cv2.destroyAllWindows()
