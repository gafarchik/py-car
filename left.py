import RPi.GPIO as GPIO

def left():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(2,GPIO.OUT)
    GPIO.output(2,True)
    GPIO.output(2,True)
