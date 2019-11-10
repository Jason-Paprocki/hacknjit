from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv
import requests
from twilio.rest import Client

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv
from twilio.rest import Client

"""account_sid = 'AC1f8226cae497269ca7a9680131a2d2af'
auth_token = '00b0091d18423f8ac406fd4c8d83e861'
client = Client(account_sid, auth_token)

"""
sid = 'AC1f8226cae497269ca7a9680131a2d2af'

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    msg_url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json'.format(sid)
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    phone_number = request.form["From"]

    count = 0

    while count < 3:
        print("received")

    resp.message(phone_number + " complete")

    #body_elements = body.split(' ')
    # Determine the right reply for this message
    '''
    if 'from' in body or 'From' in body:
        writeToCsv(phone_number)
        resp.message(str(isInFile(phone_number)))
    elif 'To' in body or 'to' in body:
        resp.message(str(writeToCsv(phone_number)))


    '''
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
