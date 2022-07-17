from TankController import TankController

class TankControllerPart:

    def __init__(self, controller: TankController) -> None:
        self.tankController = controller
        self.tankController.motorsOn()

    def run(self, moving_forward, moving_reverse, steering_left, steering_right):
        if moving_forward:
            self.tankController.moveForward()
            if steering_left:
                self.tankController.turnLeft()
            elif steering_right:
                self.tankController.turnRight
        elif moving_reverse:
            self.tankController.moveBackwards()
            if steering_left:
                self.tankController.turnLeft()
            elif steering_right:
                self.tankController.turnRight()
        elif steering_left:
            self.tankController.spinLeft()
        elif steering_right:
            self.tankController.spinRight()
        else:
            self.tankController.stop()
            