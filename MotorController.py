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
		self.leftMotorEnable = 33
		self.leftMotorPWM = None
		self.leftMotorIn1 = 35
		self.leftMotorIn2 = 37

		self.rightMotorEnable = 26
		self.rightMotorPWM = None
		self.rightMotorIn1 = 24
		self.rightMotorIn2 = 22

	def setup(self):
		print("Setting up")
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.leftMotorEnable, GPIO.OUT)
		GPIO.setup(self.leftMotorIn1, GPIO.OUT)
		GPIO.setup(self.leftMotorIn2, GPIO.OUT)
		GPIO.setup(self.rightMotorEnable, GPIO.OUT)
		GPIO.setup(self.rightMotorIn1, GPIO.OUT)
		GPIO.setup(self.rightMotorIn2, GPIO.OUT)

		print("initializing all pins to low")
		GPIO.output(self.leftMotorEnable, GPIO.LOW)
		GPIO.output(self.leftMotorIn1, GPIO.LOW)
		GPIO.output(self.leftMotorIn2, GPIO.LOW)
		GPIO.output(self.rightMotorEnable, GPIO.LOW)
		GPIO.output(self.rightMotorIn1, GPIO.LOW)
		GPIO.output(self.rightMotorIn2, GPIO.LOW)

		print("setting up pwm pins")
		self.leftMotorPWM = GPIO.PWM(self.leftMotorEnable, 1000)
		self.leftMotorPWM.start(100)
		self.rightMotorPWM = GPIO.PWM(self.rightMotorEnable, 1000)
		self.rightMotorPWM.start(75)

	def turnOffAllMotors(self):
		print("turning all motors and pins off")
		GPIO.output(self.leftMotorEnable, GPIO.LOW)
		GPIO.output(self.leftMotorIn1, GPIO.LOW)
		GPIO.output(self.leftMotorIn2, GPIO.LOW)
		GPIO.output(self.rightMotorEnable, GPIO.LOW)
		GPIO.output(self.rightMotorIn1, GPIO.LOW)
		GPIO.output(self.rightMotorIn2, GPIO.LOW)

	def cleanup(self):
		print("Cleaning up")
		self.turnOffAllMotors()
		GPIO.cleanup()

	# Motor Controlling methods
	def leftMotorOff(self):
		GPIO.output(self.leftMotorEnable, GPIO.LOW)

	def rightMotorOff(self):
		GPIO.output(self.rightMotorEnable, GPIO.LOW)

	def leftMotorOn(self):
		GPIO.output(self.leftMotorEnable, GPIO.HIGH)

	def rightMotorOn(self):
		GPIO.output(self.rightMotorEnable, GPIO.HIGH)

	def setLeftMotorSpeed(self, speed):
		self.leftMotorPWM.ChangeDutyCycle(speed)

	def setRightMotorSpeed(self, speed):
		self.rightMotorPWM.ChangeDutyCycle(speed)

	def leftMotorForward(self):
		GPIO.output(self.leftMotorIn2, GPIO.LOW)
		GPIO.output(self.leftMotorIn1, GPIO.HIGH)

	def leftMotorReverse(self):
		GPIO.output(self.leftMotorIn1, GPIO.LOW)
		GPIO.output(self.leftMotorIn2, GPIO.HIGH)

	def rightMotorForward(self):
		GPIO.output(self.rightMotorIn1, GPIO.LOW)
		GPIO.output(self.rightMotorIn2, GPIO.HIGH)

	def rightMotorReverse(self):
		GPIO.output(self.rightMotorIn2, GPIO.LOW)
		GPIO.output(self.rightMotorIn1, GPIO.HIGH)


if __name__ == '__main__':
	motorController = MotorController()
	motorController.setup()
	try:
		simpleOneWayLoop(motorController)
	except KeyboardInterrupt:
		motorController.cleanup() 
