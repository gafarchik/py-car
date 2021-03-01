import cv2
import numpy as np
camera = cv2.VideoCapture(0)
num = 0
vnum = 0
re = True
def gen_frames():  
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video():
    global re
    global vnum
    if re == False:
        return None
    else:	
	    fourcc = cv2.VideoWriter_fourcc(*'XVID')
	    out = cv2.VideoWriter('output'+str(vnum)+'.avi', fourcc, 15.0, (640,480))
	    vnum+=1
	    while True:
	        ret, frame = camera.read()
	        if ret==True:
	            frame = cv2.flip(frame,180)
	        else:
	        	break
	        out.write(frame)
	    camera.release()
	    out.release()
def stop_video():
    re == False
def take_photo():
    global num
    num+=1
    return_value, image = camera.read()
    cv2.imwrite('pycar'+str(num)+'.png', image) 
