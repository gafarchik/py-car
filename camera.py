import cv2
camera = cv2.VideoCapture(0)
num = 0
def gen_frames():  
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
def rec_video(a):
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') 
    video_writer = cv2.VideoWriter("output.avi", fourcc, 15, (680, 480))

    # record video
    while a<1:
        ret, frame = camera.read()
        if ret:
            video_writer.write(frame)

        else:
            break

    camera.release()
    video_writer.release()
    cv2.destroyAllWindows()
def take_photo():
    global num
    num+=1
    return_value, image = camera.read()
    cv2.imwrite('pycar'+str(num)+'.png', image) 
