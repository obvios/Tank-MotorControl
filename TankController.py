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

    def moveForward(self):
        """Moves both wheels in the forward direction at 100% speed"""
        self.motorController.leftMotorForward()
        self.motorController.rightMotorForward()
        
        self.motorController.setLeftMotorSpeed(100)
        self.motorController.setRightMotorSpeed(100)

    def moveBackwards(self):
        """Moves both wheels in the back direction at 100% speed"""
        self.motorController.leftMotorReverse()
        self.motorController.rightMotorReverse()
        
        self.motorController.setLeftMotorSpeed(100)
        self.motorController.setRightMotorSpeed(100)

    def spinLeft(self):
        self.motorController.leftMotorReverse()
        self.motorController.rightMotorForward()

    def spinRight(self):
        self.motorController.rightMotorReverse()
        self.motorController.leftMotorForward()

    def turnLeft(self):
        self.motorController.setLeftMotorSpeed(50)
        self.motorController.setRightMotorSpeed(100)
        self.motorController.rightMotorForward()
        self.motorController.leftMotorForward()

    def turnRight(self):
        self.motorController.setRightMotorSpeed(50)
        self.motorController.setLeftMotorSpeed(100)
        self.motorController.leftMotorForward()
        self.motorController.rightMotorForward()


def testTankDriver(tankController: TankController) -> None :
    tankController.motorsOn()
    tankController.moveForward()
    sleep(1)
    tankController.moveBackwards()
    sleep(1)
    tankController.turnLeft()
    sleep(1)
    tankController.turnRight()
    sleep(1)


if __name__ == '__main__':
    tankController = TankController()
    tankController.setup()
    try:
        # Call a test loop here. Pass tankController instance.
        testTankDriver(tankController)
    except KeyboardInterrupt:
        tankController.cleanup()