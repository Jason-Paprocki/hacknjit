from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])

def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if 'start' in body:
        resp.message(startInMessage())
    elif 'end' in body:
        resp.message(endInMessage())

    return str(resp)




def startInMessage():
    return "testing works"

def endInMessage():
    return "yert"



if __name__ == "__main__":
    app.run(debug=True)
