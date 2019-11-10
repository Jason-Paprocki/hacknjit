from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import csv
from twilio.rest import Client

"""account_sid = 'AC1f8226cae497269ca7a9680131a2d2af'
auth_token = '00b0091d18423f8ac406fd4c8d83e861'
client = Client(account_sid, auth_token)

"""
app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])

def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    phone_number = request.form["From"]

    count = 0

    while count < 3:
        print("received")

    resp.message(phone_number + " complete")

    #body_elements = body.split(' ')
    # Determine the right reply for this message
    '''
    if 'from' in body or 'From' in body:
        writeToCsv(phone_number)
        resp.message(str(isInFile(phone_number)))
    elif 'To' in body or 'to' in body:
        resp.message(str(writeToCsv(phone_number)))


    '''
    return str(resp)
    
#handling requests from the user
'''
def isInFile(phone_number):
    with open('mycsv.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        for index in range(len(lines)):
            if str(phone_number) == str(line[index][0]):
                print(lines)
                return index
        return -1
    readFile.close()

#
def writeToCsv(phone_number):
    with open('mycsv.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        if isInFile(phone_number) != -1:
            print("legit")
        else:
            print("not legit")



        #writer.writerow(row)


    writeFile.close()


#call this method for the starting location
def startInMessage(body, phone_number):
    for i in range(len(rows)):
        if (str(rows[i][0]) == str(phone_number)):
            print(rows)
            #rows[i][1] = writer.writerow(body)
            return


#call this method for the end location
def endInMessage(body):
    return True



    return False
'''

if __name__ == "__main__":
    app.run(debug=True)
