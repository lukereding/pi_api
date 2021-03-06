from flask import Flask, jsonify, make_response, render_template, request, abort
from gpiozero import CPUTemperature
import plivo, plivoxml
import os
import smtplib
from email.mime.text import MIMEText

def send_email(message, password):
    """Send reminder emails to everyone in dict_of_recipients."""
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    try:
        session.login('lukereding@gmail.com', password)
    except:
        print("could not log in")
        # sys.exit(1)
    # send the email
    msg = MIMEText(message)
    msg['Subject'] = 'text received'
    msg['From'] = 'info@lreding.com'
    msg['To'] = 'lukereding@gmail.com'
    msg = msg.as_string()
    session.sendmail('lukereding@gmail.com', 'lukereding@gmail.com', msg)
    
    
app = Flask(__name__)
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def hello():
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/temp', methods = ['GET'])
def get_temp():
    with app.app_context():
        cpu = CPUTemperature()
        return render_template('temp.html', temp = cpu.temperature)

@app.route("/receive_sms", methods=['GET','POST'])
def receive_sms():
    if not request.values.get('From'):
        abort(404)
    # Sender's phone numer
    from_number = request.values.get('From')
    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')
    # The text which was received
    text = request.values.get('Text')

    # Print the message
    print 'Message received - From: %s, To: %s, Text: %s' % (from_number, to_number, text)
    passw = os.getenv('GMAIL')
    send_email(text, passw)

    return "Message received", 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False, port = 5001)
