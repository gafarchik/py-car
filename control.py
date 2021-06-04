import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class drive:
    in1 = 26
    in2 = 19
    bin1 = 6
    bin2 = 13
    pwm = 5
    pwm1 = 21
    standbyPin = 4
    hertz = 1000
    reverse = False
    def __init__(self, in1, in2, pwm,pwm1,bin1,bin2,standbyPin, reverse):
        self.in1 = in1
        self.in2 = in2
        self.pwm = pwm
        self.pwm1 = pwm1
        self.bin1= bin1
        self.bin2 = bin2
        self.standbyPin = standbyPin
        self.reverse = reverse
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(bin1,GPIO.OUT)
        GPIO.setup(bin2,GPIO.OUT)
        GPIO.setup(pwm,GPIO.OUT)
        GPIO.setup(pwm1,GPIO.OUT)
        GPIO.setup(standbyPin,GPIO.OUT)
        GPIO.output(standbyPin,GPIO.HIGH)
        GPIO.output(pwm,GPIO.HIGH)
        GPIO.output(pwm1,GPIO.HIGH)
        GPIO.output(self.bin1,GPIO.LOW)
        GPIO.output(self.bin2,GPIO.LOW)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
    def movefor(self, speed):
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
            p = GPIO.PWM(self.pwm1,100)
            p.ChangeDutyCycle(100)
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
    def moveright(self,hertz):
        GPIO.PWM(self.pwm1,1)
        GPIO.output(self.bin1,GPIO.LOW)
        GPIO.output(self.bin2, GPIO.HIGH)
    def moveleft(self,hertz):
        GPIO.PWM(self.pwm1,1)
        GPIO.output(self.bin2,GPIO.LOW)
        GPIO.output(self.bin1,GPIO.HIGH)
    def brake(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)

    def standby(self, value):
        GPIO.output(self.standbyPin,value)

    def __del__(self):
        GPIO.cleanup()


