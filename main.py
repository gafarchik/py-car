from flask import Flask, render_template, Response, redirect, url_for, request
from camera import gen_frames, Recordvideo , take_photo
from control import allStop,forwardDrive,reverseDrive,TurnLeft,TurnRight,center
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/redirect',methods=['GET','POST'])
def redirect():
    if request.method == 'POST':
        if request.form.get('Start')== 'Start':
            return render_template('panel.html')
            return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
        elif request.form.get('start')== 'Start':
            return render_template('panel.html')
            return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
        elif request.form.get('Home')== 'Home':
            return render_template('index.html')
        elif request.form.get('Stop')=='Stop':
            return render_template('index.html')
@app.route('/',methods=['GET','POST'])
def panel():
    return render_template("panel.html")
@app.route('/movef',methods=['GET','POST'])
def movef():
    if request.method == 'POST':
        if request.form.get('forward') == '↑':
            forwardDrive()
            return render_template('panel.html')
            return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
        else:
            pass # unknown
@app.route('/moveb',methods=['GET','POST'])
def moveb():
    if request.method == 'POST':
        if request.form.get('back' )== '↓':
            reverseDrive()
            return render_template('panel.html')
            #return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/mover',methods=['GET','POST'])
def mover():
    if request.method == 'POST':
        if request.form.get('right')== '→':
            TurnRight()
            return render_template('panel.html')
            #return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/movel',methods=['GET','POST'])
def movel():
    if request.method == 'POST':
        if request.form.get('left' )== '←':
            TurnLeft()
            return render_template('panel.html')
            #return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/moves',methods=['GET','POST'])
def moves():
    if request.method == 'POST':
        if request.form.get('stop')== 'stop':
            allStop()
            return render_template('panel.html')
            #return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/movec',methods=['GET','POST'])
def movec():
    if request.method == 'POST':
        if request.form.get('center') == 'center':
            center()
            return render_template('panel.html')
            #return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/record', methods=['GET', 'POST'])
def record():
    if request.method == 'POST':
        if request.form.get('Start')== '▶':
            Recordvideo.video()
            return render_template('panel.html')
            return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
        elif request.form.get('Stop')== '■':
            Recordvideo.stop_video()
            return render_template('panel.html')
            return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
        else:
            return render_template("panel.html")
            return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/photo', methods=['GET', 'POST'])
def photo():
	if request.method == 'POST':
	    if request.form.get('Photo')== '📷':
	        take_photo()
	        return render_template('panel.html')
	        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port="7777", debug=False)#192.168.50.77
