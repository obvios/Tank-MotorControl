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

if __name__ == '__main__':
	setup()
	try:
		simpleOneWayLoop()
	except KeyboardInterrupt:
		cleanup() 
