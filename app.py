from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv
from twilio.rest import Client
import requests
import os

account_sid = 'AC1f8226cae497269ca7a9680131a2d2af'
auth_token = '00b0091d18423f8ac406fd4c8d83e861'
client = Client(account_sid, auth_token)



url = "https://api.twilio.com/2010-04-01/Accounts/AC1f8226cae497269ca7a9680131a2d2af/Messages.json"
app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])

def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    phone_number = request.form["From"]

    messages = client.messages.list()

    '''for record in messages:
        if record.from_ == phone_number:


        data[2][1] = '20.6'

        writer = csv.writer(open('mycsv.csv', 'wb'))
        writer.writerows(data)'''

    #resp.message()

    #body_elements = body.split(' ')
    # Determine the right reply for this message

    return str(resp)

def findPhoneNumber():
    with open('mycsv.csv') as csv_file:
        csv_reader = csv.reader('mycsv.csv')
        list = list(csv_reader)
        print(list)

if __name__ == "__main__":
    app.run(debug=True)
