import RPi.GPIO as GPIO

def back():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    # pin 3 out
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(2,GPIO.OUT)
    GPIO.output(3,True)
    GPIO.output(2,True)
