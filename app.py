from flask import Flask, jsonify, make_response, render_template
from gpiozero import CPUTemperature

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/temp', methods = ['GET'])
def get_temp():
    with app.app_context():
        cpu = CPUTemperature()
        return render_template('temp.html', temp = cpu.temperature)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
