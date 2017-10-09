from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import os
import errno

# this file makes queries to the inventory
# the messaging format is:
# read key: (item)
# example:
# ready key: orange
# expected output: orange: 7

def QueryItem(body):
    
    msg = "Item not found"   #default message when nothing is found
    item = body[10:]         #the item after 'read key: '
    item2 = item + ":"       #item with ":" added to it
    itemsize = len(item)     #length of item

    read = open("inventory.txt", "r")
    for line in read:
        if item2 in line[:itemsize + 1]:
            msg = line
            othermsg = line[:itemsize]
    read.close()

    #resp.message(msg)

    return str(msg)

if __name__ == "__main__":
    app.run(debug=True)
