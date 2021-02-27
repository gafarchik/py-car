from flask import Flask, render_template, Response, redirect, url_for, request
from camera import gen_frames, rec_video
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/record', methods=['GET', 'POST'])
def record():
	if request.method == 'POST':
	    if request.form.get('Start')== 'Start':
	        rec_video(1)
	        return render_template("index.html")
	    elif request.form.get('Stop')== 'Stop':
	        rec_video(0)
	        return render_template("index.html")
	    else:
	        return render_template("index.html")
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='192.168.88.218',port="7777", debug=True)
