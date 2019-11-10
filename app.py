from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv
from twilio.rest import Client
import requests
import os
import sys
from main import main
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

    body_elements = str(body).split(' ')



    if (body_elements[0] == "Go" or body_elements[0] == "go" or body_elements[0] == "GO"):
        direction = "go"
        messagebody = body_elements[1]
        proccessTask(phone_number, direction, messagebody)
    elif(body_elements[0] == "From" or body_elements[0] == "from" or body_elements[0] == "FROM"):
        direction = "from"
        messagebody = body_elements[1]
        proccessTask(phone_number, direction, messagebody)
    else:
        resp.message("This is an incorrect syntax")

    #reply to message
    #resp.message()

    return str(resp.message())
    #return str(resp.message(main(origin, destination)))

def proccessTask(phone_number, direction, messagebody):
    print(phone_number + " te diretion is: " + direction + " message: "+ messagebody)

    #opens csv file for reading
    with open('mycsv.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        print(lines)
        #iterates through whole csv file
        for index in range(len(lines)):

            # found the phone number already
            if str(phone_number) == str(lines[index][0]):
                print(index)
                # direction is go so its the first collumn
                if (direction == "from"):
                    with open('mycsv.csv', 'w') as writeFile:
                        print(index)
                        lines[index] = [lines[index][0], str(messagebody), lines[index][2]]
                        writer = csv.writer(writeFile)
                        writer.writerow(lines)
                        return
                # direction is end point so its the second collumn
                else:
                    with open('mycsv.csv', 'w') as writeFile:
                        print(index)
                        print(lines[index])
                        lines[index] = [lines[index][0], lines[index][1], str(messagebody)]
                        writer = csv.writer(writeFile)
                        writer.writerow(lines)
                        return

            # phone number doesnt exist so it adds the phone number with the message data
            else:
                # direction is go so its the first collumn
                if (direction == "go"):
                    with open('mycsv.csv', "a") as appendFile:
                        writer = csv.writer(appendFile)
                        templine = [str(phone_number), '', str(messagebody)]
                        writer.writerow(templine)
                        return

                # direction is end point so its the second collumn
                else:
                    with open('mycsv.csv', "a") as appendFile:
                        writer = csv.writer(appendFile)
                        templine = [str(phone_number), str(messagebody), '']
                        writer.writerow(templine)
                        return





if __name__ == "__main__":
    app.run(debug=True)
