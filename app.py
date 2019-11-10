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
    if 'Start' in body:
        print("yteqg")
    elif 'end' in body:
        resp.message(endInMessage())

    return str(resp)



def startInMessage():
    return "testing works"

def endInMessage():
    return "yert"

def phoneNumberHandler(phone_number):
    rows = list(csv_f)

    for row in rows:
        if (str(rows[row][0]) == str(phone_number)):
            print(row)
            print("beep")
if __name__ == "__main__":
    app.run(debug=True)
