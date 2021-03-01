import cv2
import numpy as np
camera = cv2.VideoCapture(0)
num = 0
vnum = 0
vcheck = 1
def gen_frames():  
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
def stop_video():
    global vcheck
    vcheck -=1
    print(vcheck)
def video():
    global vcheck
    global vnum
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output'+str(vnum)+'.avi', fourcc, 15.0, (640,480))
    vnum+=1
    while vcheck==1:
        ret, frame = camera.read()
        if ret==True:
            frame = cv2.flip(frame,180)
        out.write(frame)
        if vcheck == 0:
        	break
    camera.release()
    out.release()
def take_photo():
    global num
    num+=1
    return_value, image = camera.read()
    cv2.imwrite('pycar'+str(num)+'.png', image) 
