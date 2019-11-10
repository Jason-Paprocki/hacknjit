from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv
from twilio.rest import Client
import requests
import os
import sys

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
    direction = ""
    # Start our TwiML response
    resp = MessagingResponse()

    phone_number = request.form["From"]

    messages = client.messages.list()

    body_elements = body.split(' ')



    if (body_elements[0] == "go"):
        print("beep")
        direction = "go"
        messagebody = body[1]
        findPhoneNumber(phone_number, direction, messagebody)
        print("beep2")
    elif(body_elements[0] == "from"):
        direction = "from"
        messagebody = body[1]
        findPhoneNumber(phone_number, direction, messagebody)
    else:
        resp.message("This is an incorrect syntax")

    #reply to message
    #resp.message()
    return str(resp)

def findPhoneNumber(phone_number, direction, messagebody):
    print(phone_number + direction + messagebody)
    row=[]
    #opens csv file for reading
    with open('mycsv.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        print(lines)

        #iterates through whole csv file
        for index in range(len(lines)):
            #found the phone number already
            if str(phone_number) == lines[index][0]:

                #direction is go so its the first collumn
                if (direction == "from"):
                    with open('mycsv.csv', 'w') as writeFile:
                        row[index][1] = messagebody
                        writer = csv.writer(row)

                #direction is end point so its the second collumn
                else:
                    with open('mycsv.csv', 'w') as writeFile:
                        row[index][2] = messagebody
                        writer = csv.writer(row)
            #phone number doesnt exist so it adds the phone number with the message data
            else:
                #direction is go so its the first collumn
                if (direction == "go"):
                    with open('mycsv.csv', 'a') as appendFile:
                        row[len(lines)][1] = messagebody
                        writer = csv.writer(row)
                #direction is end point so its the second collumn
                else:
                    with open('mycsv.csv', 'a') as appendFile:
                        row[len(lines)][2] = messagebody
                        writer = csv.writer(row)





if __name__ == "__main__":
    app.run(debug=True)
