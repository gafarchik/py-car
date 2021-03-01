from flask import Flask, render_template, Response, redirect, url_for, request
from camera import gen_frames, rec_video, take_photo
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/record', methods=['GET', 'POST'])
def record():
	if request.method == 'POST':
	    if request.form.get('Start')== 'Start':
	        rec_video(1)
	        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
	    elif request.form.get('Stop')== 'Stop':
	        rec_video(0)
	        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
	    else:
	        return render_template("index.html")
@app.route('/photo', methods=['GET', 'POST'])
def photo():
	if request.method == 'POST':
	    if request.form.get('Photo')== 'Photo':
	        take_photo()
	        return render_template('index.html')
	        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='192.168.0.108',port="7777", debug=True)
