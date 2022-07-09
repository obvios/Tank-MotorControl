import RPi.GPIO as GPIO
from time import sleep

# Motor 1
pwmPin = None
enablePin = 33
motorControl1 = 35
motorControl2 = 37

# Motor 2
pwmPin2 = None
enablePin2 = 26
motorControl1_2 = 24
motorControl2_2 = 22

# Setup
def setup():
	print("Setting up")
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(enablePin, GPIO.OUT)
	GPIO.setup(motorControl1, GPIO.OUT)
	GPIO.setup(motorControl2, GPIO.OUT)
	GPIO.setup(enablePin2, GPIO.OUT)
	GPIO.setup(motorControl1_2, GPIO.OUT)
	GPIO.setup(motorControl2_2, GPIO.OUT)


	print("initializing pins to low")
	GPIO.output(enablePin, GPIO.LOW)
	GPIO.output(motorControl1, GPIO.LOW)
	GPIO.output(motorControl2, GPIO.LOW)
	GPIO.output(enablePin2, GPIO.LOW)
	GPIO.output(motorControl1_2, GPIO.LOW)
	GPIO.output(motorControl2_2, GPIO.LOW)

	# set PWM for enablePin
	global pwmPin, pwmPin2
	pwmPin = GPIO.PWM(enablePin, 1000)
	pwmPin.start(75)
	pwmPin2 = GPIO.PWM(enablePin2, 1000)
	pwmPin2.start(75)
	

def turnOffAllMotors():
	print("turning all motors and pins off")
	GPIO.output(enablePin, GPIO.LOW)
	GPIO.output(motorControl1, GPIO.LOW)
	GPIO.output(motorControl2, GPIO.LOW)
	GPIO.output(enablePin2, GPIO.LOW)
	GPIO.output(motorControl1_2, GPIO.LOW)
	GPIO.output(motorControl2_2, GPIO.LOW)

def cleanup():
	print("Cleaning up")
	turnOffAllMotors()
	GPIO.cleanup()

def changePWMValue(value):
	global pwmPin, pwmPin2
	pwmPin.ChangeDutyCycle(value)
	pwmPin2.ChangeDutyCycle(value)

def simpleOneWayLoop():
	print("starting one way loop")
	GPIO.output(enablePin, GPIO.HIGH)
	GPIO.output(enablePin2, GPIO.HIGH)
	while True:
		print("forward")
		GPIO.output(motorControl2, GPIO.LOW)
		GPIO.output(motorControl1, GPIO.HIGH)
		GPIO.output(motorControl1_2, GPIO.LOW)
		GPIO.output(motorControl2_2, GPIO.HIGH)
		sleep(5)

		print("slowwing down")
		changePWMValue(50)
		sleep(5)

		print("speeding up")
		changePWMValue(75)
		sleep(5)

		print("backward")
		GPIO.output(motorControl1, GPIO.LOW)
		GPIO.output(motorControl2, GPIO.HIGH)
		GPIO.output(motorControl2_2, GPIO.LOW)
		GPIO.output(motorControl1_2, GPIO.HIGH)
		sleep(5)

		print("slowwing down")
		changePWMValue(50)
		sleep(5)

		print("speeding up")
		changePWMValue(75)
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
		self.leftMotorPWM = GPIO.PWM(enablePin, 1000)
		self.leftMotorPWM.start(100)
		self.rightMotorPWM = GPIO.PWM(enablePin2, 1000)
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
	def motorsOff(self):
		GPIO.output(self.leftMotorEnable, GPIO.LOW)
		GPIO.output(self.rightMotorEnable, GPIO.LOW)

	def motorsOn(self):
		GPIO.output(self.leftMotorEnable, GPIO.HIGH)
		GPIO.output(self.rightMotorEnable, GPIO.HIGH)

	def setLeftMotorSpeed(self, speed):
		self.leftMotorPWM.ChangeDutyCycle(speed)

	def setRightMotorSpeed(self, speed):
		self.rightMotorPWM.ChangeDutyCycle(speed)


if __name__ == '__main__':
	setup()
	try:
		simpleOneWayLoop()
	except KeyboardInterrupt:
		cleanup() 
