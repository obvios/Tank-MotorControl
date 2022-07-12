# Module to abstract the two dc motors to be controlled by the tank
import RPi.GPIO as GPIO
from time import sleep

# Used to test connections
def simpleOneWayLoop(controller):
	print("starting loop")
	controller.leftMotorOn()
	controller.rightMotorOn()

	while True:
		print("forward")
		controller.leftMotorForward()
		controller.rightMotorForward()
		print("speeding up")
		controller.setLeftMotorSpeed(100)
		controller.setRightMotorSpeed(100)
		sleep(5)

		print("slowing down")
		controller.setLeftMotorSpeed(50)
		controller.setRightMotorSpeed(50)
		sleep(5)

		print("speeding up")
		controller.setLeftMotorSpeed(100)
		controller.setRightMotorSpeed(100)
		sleep(5)

		print("backward")
		controller.leftMotorReverse()
		controller.rightMotorReverse()
		sleep(5)

		print("slowing down")
		controller.setLeftMotorSpeed(50)
		controller.setRightMotorSpeed(50)
		sleep(5)

		print("speeding up")
		controller.setLeftMotorSpeed(100)
		controller.setRightMotorSpeed(100)
		sleep(5)

class MotorController:

	def __init__(self) -> None:
		"""Defines internal variables. Maps internal variables to pins on Raspberry Pi 3+."""
		self.__leftMotorEnable = 33
		self.__leftMotorPWM = None
		self.__leftMotorIn1 = 35
		self.__leftMotorIn2 = 37

		self.__rightMotorEnable = 26
		self.__rightMotorPWM = None
		self.__rightMotorIn1 = 24
		self.__rightMotorIn2 = 22

	def setup(self):
		"""Initializes GPIO mode to BOARD. Sets all pins to OUT. All pins started on LOW. PWM pins started at 100%."""
		print("Setting up")
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.__leftMotorEnable, GPIO.OUT)
		GPIO.setup(self.__leftMotorIn1, GPIO.OUT)
		GPIO.setup(self.__leftMotorIn2, GPIO.OUT)
		GPIO.setup(self.__rightMotorEnable, GPIO.OUT)
		GPIO.setup(self.__rightMotorIn1, GPIO.OUT)
		GPIO.setup(self.__rightMotorIn2, GPIO.OUT)

		print("initializing all pins to low")
		GPIO.output(self.__leftMotorEnable, GPIO.LOW)
		GPIO.output(self.__leftMotorIn1, GPIO.LOW)
		GPIO.output(self.__leftMotorIn2, GPIO.LOW)
		GPIO.output(self.__rightMotorEnable, GPIO.LOW)
		GPIO.output(self.__rightMotorIn1, GPIO.LOW)
		GPIO.output(self.__rightMotorIn2, GPIO.LOW)

		print("setting up pwm pins")
		self.__leftMotorPWM = GPIO.PWM(self.__leftMotorEnable, 1000)
		self.__leftMotorPWM.start(100)
		self.__rightMotorPWM = GPIO.PWM(self.__rightMotorEnable, 1000)
		self.__rightMotorPWM.start(100)

	def turnOffAllMotors(self):
		print("turning all motors and pins off")
		GPIO.output(self.__leftMotorEnable, GPIO.LOW)
		GPIO.output(self.__leftMotorIn1, GPIO.LOW)
		GPIO.output(self.__leftMotorIn2, GPIO.LOW)
		GPIO.output(self.__rightMotorEnable, GPIO.LOW)
		GPIO.output(self.__rightMotorIn1, GPIO.LOW)
		GPIO.output(self.__rightMotorIn2, GPIO.LOW)

	def cleanup(self):
		print("Cleaning up")
		self.turnOffAllMotors()
		GPIO.cleanup()

	# Motor Controlling methods
	def leftMotorOff(self):
		GPIO.output(self.__leftMotorEnable, GPIO.LOW)

	def rightMotorOff(self):
		GPIO.output(self.__rightMotorEnable, GPIO.LOW)

	def leftMotorOn(self):
		GPIO.output(self.__leftMotorEnable, GPIO.HIGH)

	def rightMotorOn(self):
		GPIO.output(self.__rightMotorEnable, GPIO.HIGH)

	def setLeftMotorSpeed(self, speed: int):
		self.__leftMotorPWM.ChangeDutyCycle(speed)

	def setRightMotorSpeed(self, speed: int):
		self.__rightMotorPWM.ChangeDutyCycle(speed)

	def leftMotorForward(self):
		GPIO.output(self.__leftMotorIn2, GPIO.LOW)
		GPIO.output(self.__leftMotorIn1, GPIO.HIGH)

	def leftMotorReverse(self):
		GPIO.output(self.__leftMotorIn1, GPIO.LOW)
		GPIO.output(self.__leftMotorIn2, GPIO.HIGH)

	def rightMotorForward(self):
		GPIO.output(self.__rightMotorIn1, GPIO.LOW)
		GPIO.output(self.__rightMotorIn2, GPIO.HIGH)

	def rightMotorReverse(self):
		GPIO.output(self.__rightMotorIn2, GPIO.LOW)
		GPIO.output(self.__rightMotorIn1, GPIO.HIGH)


if __name__ == '__main__':
	motorController = MotorController()
	motorController.setup()
	try:
		simpleOneWayLoop(motorController)
	except KeyboardInterrupt:
		motorController.cleanup() 
