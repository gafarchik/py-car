import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class drive:
	in1 = 26
	in2 = 13
	pwm = 21
	pwm1 = 5
	standbyPin = 4

	#Defaults
	hertz = 1000
	reverse = False #Reverse flips the direction of the motor

	#Constructor
	def __init__(self, in1, in2, pwm, pwm1,standbyPin, reverse):
		self.in1 = in1
		self.in2 = in2
		self.pwm1 = pwm1 
		self.pwm = pwm
		self.standbyPin = standbyPin
		self.reverse = reverse

		GPIO.setup(in1,GPIO.OUT)
		GPIO.setup(in2,GPIO.OUT)
		GPIO.setup(pwm,GPIO.OUT)
		GPIO.setup(pwm1,GPIO.OUT)
		GPIO.setup(standbyPin,GPIO.OUT)
		GPIO.output(standbyPin,GPIO.HIGH)

	#Speed from -100 to 100
	def movefor(self, speed):
		#Negative speed for reverse, positive for forward
		#If necessary use reverse parameter in constructor
		dutyCycle = speed
		if(speed < 0):
			dutyCycle = dutyCycle * -1

		if(self.reverse):
			speed = speed * -1

		if(speed > 0):
			GPIO.output(self.in1,GPIO.HIGH)
			GPIO.output(self.in2,GPIO.LOW)
	def moveback(self,speed):
		dutyCycle = speed
		if(speed < 0):
			dutyCycle = dutyCycle * -1

		if(self.reverse):
			speed = speed * -1

		if(speed > 0):
			GPIO.output(self.in1,GPIO.LOW)
			GPIO.output(self.in2,GPIO.HIGH)
	def moveright():
		self.p = GPIO.PWM(pwm1, self.hertz)
		self.p.start(1)
	def moveleft():
		self.p = GPIO.PWM(pwm, self.hertz)
		self.p.start(1)
	def brake(self):
		self.p.ChangeDutyCycle(0)
		GPIO.output(self.in1,GPIO.HIGH)
		GPIO.output(self.in2,GPIO.HIGH)

	def standby(self, value):
		self.p.ChangeDutyCycle(0)
		GPIO.output(self.standbyPin,value)

	def __del__(self):
		GPIO.cleanup()
