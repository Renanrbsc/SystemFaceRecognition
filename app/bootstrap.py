from app.Controller.Controller_recognition import ControllerRecognition


class Startup:
    def __init__(self, defined_platform):
        self.recognition_controller: ControllerRecognition = defined_platform

    @classmethod
    def define_platform(cls):
        print("0 - Windows\n" \
              "-1 - Linux\n")
        platform = int(input("Informe o tipo de sistema utilizado: "))
        defined_platform = ControllerRecognition(platform)
        return cls(defined_platform)

    def initial_menu(self):
        self.recognition_controller.face_detection_cascade()
