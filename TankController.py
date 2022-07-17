# Module to abstract upon MotorController.py to control the movement of the tank
from MotorController import MotorController
from time import sleep

class TankController:
    
    def __init__(self) -> None:
        self.motorController = MotorController()

    def setup(self):
        self.motorController.setup()

    def cleanup(self):
        self.motorController.cleanup()

    def motorsOn(self):
        self.motorController.leftMotorOn()
        self.motorController.rightMotorOn()

    def motorsOff(self):
        self.motorController.leftMotorOff()
        self.motorController.rightMotorOff()

    def stop(self):
        self.motorController.setLeftMotorSpeed(0)
        self.motorController.setRightMotorSpeed(0)

    def accelerate(self):
        self.motorController.setLeftMotorSpeed(100)
        self.motorController.setRightMotorSpeed(100)

    def moveForward(self):
        """Moves both wheels in the forward direction at 100% speed"""
        self.motorController.leftMotorForward()
        self.motorController.rightMotorForward()

    def moveBackwards(self):
        """Moves both wheels in the back direction at 100% speed"""
        self.motorController.leftMotorReverse()
        self.motorController.rightMotorReverse()

    # TODO remove
    def spinLeft(self):
        self.motorController.leftMotorReverse()
        self.motorController.rightMotorForward()

    # TODO remove
    def spinRight(self):
        self.motorController.rightMotorReverse()
        self.motorController.leftMotorForward()

    def turnLeft(self):
        self.motorController.leftMotorReverse()
        self.motorController.rightMotorForward()

    def turnRight(self):
        self.motorController.rightMotorReverse()
        self.motorController.leftMotorForward()


def testTankDriver(tankController: TankController) -> None :
    tankController.motorsOn()
    tankController.moveForward()
    sleep(1)
    tankController.moveBackwards()
    sleep(1)
    tankController.spinLeft()
    sleep(1)
    tankController.spinRight()
    sleep(1)
    tankController.cleanup()


if __name__ == '__main__':
    tankController = TankController()
    tankController.setup()
    try:
        # Call a test loop here. Pass tankController instance.
        testTankDriver(tankController)
    except KeyboardInterrupt:
        tankController.cleanup()