# Module to abstract upon MotorController.py to control the movement of the tank
from MotorController import MotorController

class TankController:
    
    def __init__(self) -> None:
        self.motorController = MotorController()

    def setup(self):
        self.motorController.setup()

    def cleanup(self):
        self.motorController.cleanup()