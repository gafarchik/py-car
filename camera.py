#import cv2
#import numpy as np
#camera = cv2.VideoCapture(0)
#num = 0
#vnum = 0
#frontalface = cv2.CascadeClassifier('./cascades/frontalface.xml')
def gen_frames():
    print("video")
'''  
        while True:
            success, frame = camera.read()
            frame = cv2.flip(frame, 1)
            if not success:
                break
            else:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frontalfaces = frontalface.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in frontalfaces:
                    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]
                    cv2.putText(frame,'People', (x,y-8), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2)
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                '''
class Recordvideo():	
    def video():
        print("record")
        '''
        global vnum
        global out
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output'+str(vnum)+'.avi', fourcc, 30.0, (640,480))
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
        '''
    def stop_video():
        print("stop_record")
        '''
        global out
        out.release()
        '''
def take_photo():
    print("photo")
    '''
    global num
    num+=1
    return_value, image = camera.read()
    cv2.imwrite('pycar'+str(num)+'.png', image) 
    '''
