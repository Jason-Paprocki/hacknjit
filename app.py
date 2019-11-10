import json
from flask import Flask, request, redirect
from datetime import datetime, timedelta
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)


    #get the cookie value, or default to zero
    messagecount = int(request.cookies.get('messagecount',0))
    messagecount += 1

    twml = twiml.Response()
    twml.message("You've sent " + str(messagecount) + " messages in this conversation so far")

    resp = make_response(str(twml))

    expires=datetime.utcnow() + timedelta(hours=4)
    resp.set_cookie('messagecount',value=str(messagecount),expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))


'''

    parsed_json = json.loads(body)
    json.dump(parsed_json, indent=4)


    message_data =
    {
        "service": "gas"
        "start":
        "end":
    }
'''




    # Start our TwiML response
    resp = MessagingResponse()
    #reply for this message
    resp.message(body)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
