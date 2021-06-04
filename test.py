from control import *
from time import sleep
test = drive
print("forward")
test.movefor(100)
sleep(1)
print("back")
test.moveback(100)
sleep(1)
print("right")
test.moveright()
sleep(1)
print("left")
test.moveleft()
sleep(1)
print("brake")
test.brake()
sleep(1)

test.standby(True)
test.standby(False)