from control import *
test = drive(26,19,5,21,6,13,4,False)
def forward():
    print("forward")
    test.movefor(100)
def back():
    print("back")
    test.moveback(100)
def right():
    print("right")
    test.moveright()
def left():
    print("left")
    test.moveleft()
def brake():
    print("brake")
    test.brake()
def center():
	print("center")
	test.center()
