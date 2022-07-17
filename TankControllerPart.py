from TankController import TankController

class TankControllerPart:

    def __init__(self, controller: TankController) -> None:
        self.tankController = controller
        self.tankController.motorsOn()

    def run(self, throttle_pressed, reverse_throttle_pressed, steering_left, steering_right):
        if throttle_pressed:
            self.tankController.accelerate()
            self.tankController.moveForward()
            if steering_left:
                self.tankController.turnLeftForward()
            elif steering_right:
                self.tankController.turnRightForward()
        elif reverse_throttle_pressed:
            self.tankController.accelerate()
            self.tankController.moveBackwards()
            if steering_left:
                self.tankController.turnLeft()
            elif steering_right:
                self.tankController.turnRight()
        else:
            self.tankController.stop()

    def shutdown(self):
        self.tankController.motorsOff()
        self.tankController.cleanup()
            
