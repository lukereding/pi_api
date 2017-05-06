from flask import Flask, jsonify, make_response
#from gpiozero import CPUTemperature

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/temp', methods = ['GET'])
def get_temp():
    cpu = CPUTemperature()
    return jsonify(cpu.temperature)

if __name__ == '__main__':
    app.run()
