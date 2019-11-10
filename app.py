from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv
from twilio.rest import Client

account_sid = 'AC1f8226cae497269ca7a9680131a2d2af'
auth_token = '00b0091d18423f8ac406fd4c8d83e861'
client = Client(account_sid, auth_token)


f = open('mycsv.csv')
csv_f = csv.reader(f)


app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])

def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    phone_number = request.form["From"]
    phoneNumberHandler(phone_number)

    # Determine the right reply for this message
    if 'Start' in body or 'start' in body:
        startInMessage(body)
    elif 'end' in body or 'End' in body:
        resp.message(endInMessage())

    return str(resp)

#handling requests from the user
rows = list(csv_f)

#call this method for the starting location
def startInMessage(body):
    return True

#call this method for the end location
def endInMessage(body):
    return True

#this will handle the phone number
def phoneNumberHandler(phone_number):
    for i in range(len(rows)):
        if (str(rows[i][0]) == str(phone_number)):

            if (startInMessage()):
                rows[i][1] = message
            if endInMessage():
                return

    return False

if __name__ == "__main__":
    app.run(debug=True)
