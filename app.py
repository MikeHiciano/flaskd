'''
    programa de diana , terminar lo basico
'''
from flask import Flask ,render_template , url_for, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
        return render_template('main.html')

@app.route('/room1on', methods=["POST"])
def room1on():
        name = "turning on!"
        return render_template("main.html", name=name)
@app.route('/room1off', methods=["POST"])
def room1off():
        name = "turning off!"
        return render_template("main.html", name=name)

if __name__ == '__main__':
    app.run()