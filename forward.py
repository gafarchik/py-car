import RPi.GPIO as GPIO

def forward():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    # pin 1 output
    GPIO.setup(1,GPIO.OUT)
    GPIO.setup(2,GPIO.OUT) 
    GPIO.output(1,True)
    GPIO.output(2,True)