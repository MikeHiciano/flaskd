'''
    Hasta ahora funcionan 3 habitaciones

    things to do:

    -adaptar codigo para raspberry pi
    -anadir demas parametros
    -mejorar la estetica
    
'''
from flask import Flask ,render_template , url_for, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
        return render_template('main.html')

@app.route('/room1on', methods=["POST"])
def room1on():
        name = "Room 1 on!"
        return render_template("main.html", name=name)

@app.route('/room1off', methods=["POST"])
def room1off():
        name = "Room 1 off!"
        return render_template("main.html", name=name)

@app.route('/room2on', methods=["POST"])
def room2on():
        name = "Room 2 on!"
        return render_template("main.html", name=name)

@app.route('/room2off', methods=["POST"])
def room2off():
        name = "Room 2 off!"
        return render_template("main.html", name=name)

@app.route('/room3on', methods=["POST"])
def room3on():
        name = "Room 3 on!"
        return render_template("main.html", name=name)

@app.route('/room3off', methods=["POST"])
def room3off():
        name = "Room 3 off!"
        return render_template("main.html", name=name)

@app.route('/kitchenon', methods=["POST"])
def kitchenon():
        name = "Kitchen on!"
        return render_template("main.html", name=name)

@app.route('/kitchenoff', methods=["POST"])
def kitchenoff():
        name = "Kitchen off!"
        return render_template("main.html", name=name)

@app.route('/livingon', methods=["POST"])
def livingon():
        name = "Living room on!"
        return render_template("main.html", name=name)

@app.route('/livingoff', methods=["POST"])
def livingoff():
        name = "Living room off!"
        return render_template("main.html", name=name)

@app.route('/garageon', methods=["POST"])
def garageon():
        name = "Garage on!"
        return render_template("main.html", name=name)

@app.route('/garageoff', methods=["POST"])
def garageoff():
        name = "Garage off!"
        return render_template("main.html", name=name)

@app.route('/tv1on', methods=["POST"])
def tvoneon():
        name = "TV #1 on!"
        return render_template("main.html", name=name)

@app.route('/tv1off', methods=["POST"])
def tvoneoff():
        name = "TV #1 off!"
        return render_template("main.html", name=name)

@app.route('/tv2on', methods=["POST"])
def tvtwoon():
        name = "TV #2 on!"
        return render_template("main.html", name=name)

@app.route('/tv2off', methods=["POST"])
def tvtwooff():
        name = "TV #2 off!"
        return render_template("main.html", name=name)

if __name__ == '__main__':
    app.run()