import os
from flask import Flask, render_template, jsonify, request, Response
from flask_bootstrap import Bootstrap
from camera import VideoCamera
from bson.json_util import loads, dumps

# APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is my secret key!'
Bootstrap(app)

# Static path
static_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"))


# LANDING
@app.route('/')
def index():
	return render_template('index.html')


# INFO
@app.route('/info')
def info():
	return render_template('info.html')


# PICTURE
@app.route('/picture')
def picture():
	return render_template('picture.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# SUCCESS
@app.route('/success')
def success():
	return render_template('success.html')


# MAP
@app.route('/map')
def map():

	return render_template('map.html')


# ATMs
@app.route('/atms')
def atms():

	# Read
	with open(os.path.join(static_path, 'data', 'atms.json')) as f:  
		data = loads(f.read())
	# Features
	features = []
	for line in data:
		postal_address = line['Location']['PostalAddress']
		address = ', '.join([ p for p in postal_address['AddressLine'] if p != '.' ]).title()
		geolocation = postal_address['GeoLocation']['GeographicCoordinates']
		features.append({
        	"type": "Feature",
        	"properties":  {
            	'category': 'ATM',
            	'popupContent': '<strong> ATM </strong>',
				'address': address,

        	},
        	"geometry": {
          		"type": "Point",
          		"coordinates": [ float(geolocation['Longitude']), float(geolocation['Latitude']) ]
        	}
		})
	return dumps(features)


# CHECK
@app.route('/check')
def check():
	return render_template('check.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)