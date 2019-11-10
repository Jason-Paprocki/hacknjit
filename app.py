from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv
from twilio.rest import Client

account_sid = 'AC1f8226cae497269ca7a9680131a2d2af'
auth_token = '00b0091d18423f8ac406fd4c8d83e861'
client = Client(account_sid, auth_token)


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
        testing = ''
        all_messages = client.messages.list(limit=10)
        for m in all_messages:
            testing += all_messages
        resp.message('There are {} messages in your account.'.format(len(testing)))
    elif 'end' in body:
        resp.message(endInMessage())

    return str(resp)




def startInMessage():
    return "testing works"

def endInMessage():
    return "yert"



if __name__ == "__main__":
    app.run(debug=True)
