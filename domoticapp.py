'''
     Codigo adaptado para la raspberry pi

    este codigo es exclusivamente para la funcion de backend
    para casa domotica.

'''
from flask import Flask ,render_template , url_for, request
import RPi.GPIO as GPIO

#como estan organizados los GPIO's
room1 = 17
room2 = 4
room3 = 27
living = 22
kitchen = 18
garage = 23
tv1 = 24
tv2 = 25

salidas = [room1,room2,room3,living,kitchen,garage,tv1,tv2]

GPIO.setmode(GPIO.BCM)

for i in range(8):
    GPIO.setup(salidas[i],GPIO.OUT)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
        return render_template('main.html')

@app.route('/room1on', methods=["POST"])
def room1on():
        name = "Room 1 on!"
        GPIO.output(room1,GPIO.HIGH)
        return render_template("main.html", name=name)
        

@app.route('/room1off', methods=["POST"])
def room1off():
        name = "Room 1 off!"
        GPIO.output(room1,GPIO.LOW)
        return render_template("main.html", name=name)
        

@app.route('/room2on', methods=["POST"])
def room2on():
        name = "Room 2 on!"
        GPIO.output(room2,GPIO.HIGH)
        return render_template("main.html", name=name)

@app.route('/room2off', methods=["POST"])
def room2off():
        name = "Room 2 off!"
        GPIO.output(room2,GPIO.LOW)
        return render_template("main.html", name=name)

@app.route('/room3on', methods=["POST"])
def room3on():
        name = "Room 3 on!"
        GPIO.output(room3,GPIO.HIGH)
        return render_template("main.html", name=name)

@app.route('/room3off', methods=["POST"])
def room3off():
        name = "Room 3 off!"
        GPIO.output(room3,GPIO.LOW)
        return render_template("main.html", name=name)

@app.route('/kitchenon', methods=["POST"])
def kitchenon():
        name = "Kitchen on!"
        GPIO.output(kitchen,GPIO.HIGH)
        return render_template("main.html", name=name)

@app.route('/kitchenoff', methods=["POST"])
def kitchenoff():
        name = "Kitchen off!"
        GPIO.output(kitchen,GPIO.LOW)
        return render_template("main.html", name=name)

@app.route('/livingon', methods=["POST"])
def livingon():
        name = "Living room on!"
        GPIO.output(living,GPIO.HIGH)
        return render_template("main.html", name=name)

@app.route('/livingoff', methods=["POST"])
def livingoff():
        name = "Living room off!"
        GPIO.output(living,GPIO.LOW)
        return render_template("main.html", name=name)

@app.route('/garageon', methods=["POST"])
def garageon():
        name = "Garage on!"
        GPIO.output(garage,GPIO.HIGH)
        return render_template("main.html", name=name)

@app.route('/garageoff', methods=["POST"])
def garageoff():
        name = "Garage off!"
        GPIO.output(garage,GPIO.LOW)
        return render_template("main.html", name=name)

@app.route('/tv1on', methods=["POST"])
def tvoneon():
        name = "TV #1 on!"
        GPIO.output(tv1,GPIO.HIGH)
        return render_template("main.html", name=name)

@app.route('/tv1off', methods=["POST"])
def tvoneoff():
        name = "TV #1 off!"
        GPIO.output(tv1,GPIO.LOW)
        return render_template("main.html", name=name)

@app.route('/tv2on', methods=["POST"])
def tvtwoon():
        name = "TV #2 on!"
        GPIO.output(tv2,GPIO.HIGH)
        return render_template("main.html", name=name)

@app.route('/tv2off', methods=["POST"])
def tvtwooff():
        name = "TV #2 off!"
        GPIO.output(tv2,GPIO.LOW)
        return render_template("main.html", name=name)

if __name__ == '__main__':
    app.run(debug = "True", host = "0.0.0.0")