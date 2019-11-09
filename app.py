import json
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # writing JSON object
    with open('data.json', 'w') as f:
        json.dump(resp, f)


    #reply for this message
    resp.message("hello")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
