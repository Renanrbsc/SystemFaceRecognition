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

    def redimension_image(self):
        self.image = cv2.flip(self.image, 0)  # Flip vertically
        self.image = cv2.rotate(self.image, cv2.ROTATE_180)  # Rotate vertically
        return self.image

    def title_screen(self):
        cv2.imshow('Facial Recognition System', self.image)

    def close_screen(self):
        if cv2.waitKey(30) == 27:
            if input("press 'Q' to quit: ") == 'Q':
                return True
        return False

    def release(self):
        self.video_capture.release()

    def close_all_windows(self):
        cv2.destroyAllWindows()
