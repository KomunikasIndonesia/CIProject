from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml

import os
import errno
import QueryItem as qi
import AddItem as ai

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms():

    number = request.form['From']
    body = request.form['Body']
    body = body.lower()

    resp = MessagingResponse()

    #inventory query
    if body[0:9] == 'read key:':
        msg = qi.QueryItem(body)
    #add to inventory
    elif body[0:10] == 'store key:':
        msg = ai.AddItem(body)
        
    #add more here

    j = open('test.txt', 'w')
    j.write(msg + "\n")
    j.close

    resp.message(msg)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
