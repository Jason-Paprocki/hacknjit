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

    parsed_json = json.loads(body)
    json.dump(parsed_json, indent=4)

    """
    End goal JSON file:
    {
        "service": "gas"
        "start":
        "end":
    }
    """

    #reply for this message
    resp.message(body)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
