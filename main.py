from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import os
import errno

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms():

    number = request.form['From']
    body = request.form['Body']
    body = body.lower()

    resp = MessagingResponse()

    #inventory query
    if body[0:9] == 'read key:':

    #add to inventory
    elif body[0:10] == 'store key:':

    #add more here

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
