from TankController import TankController

class TankControllerPart:

    def __init__(self, controller: TankController) -> None:
        self.tankController = controller

    def run(self, moving_forward, moving_reverse, steering_left, steering_right):
        pass