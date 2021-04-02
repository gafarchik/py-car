import RPi.GPIO as GPIO

def right():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(1,GPIO.OUT)
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(1,True)
    GPIO.output(4,True)