from flask import Flask, Response, request, jsonify
from flask import Flask, render_template
import threading
import json
import websocket
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

frame_lock = threading.Lock()
frame_data = None

linear_speed = 0
angular_speed = 0
speed_increase_percentage = 5

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/increaseAngularSpeed')
def f1():
    global angular_speed
    angular_speed += speed_increase_percentage
    angular_speed = min(angular_speed, 10)
    return jsonify({"angular_speed":angular_speed, "linear_speed":linear_speed})

@app.route('/decreaseAngularSpeed')
def f2():
    global angular_speed
    angular_speed -= speed_increase_percentage
    angular_speed = max(angular_speed, 0)
    return jsonify({"angular_speed":angular_speed, "linear_speed":linear_speed})

@app.route('/increaseLinearSpeed')
def f3():
    global linear_speed
    linear_speed += speed_increase_percentage
    linear_speed = min(linear_speed, 30)
    return jsonify({"angular_speed":angular_speed, "linear_speed":linear_speed})

@app.route('/decreaseLinearSpeed')
def f4():
    global linear_speed
    linear_speed -= speed_increase_percentage
    linear_speed = max(linear_speed, 0)
    return jsonify({"angular_speed":angular_speed, "linear_speed":linear_speed})

@app.route('/stop')
def f5():
    global linear_speed, angular_speed
    linear_speed = 0
    angular_speed = 0
    return jsonify({"angular_speed":angular_speed, "linear_speed":linear_speed})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
