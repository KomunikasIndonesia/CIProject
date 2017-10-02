from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import os
import errno


def AddItem():

    write = open("inventory.txt", "r")
    lines = write.readlines()
    write.close()

    item = body[11:]               #text after 'store key: '
    itemsize = len(item)           #size of text after 'store key: '
    numbegin = item.find(":")      #finds where the ':' character is
    quantity = item[numbegin + 2:] #gets characters after ':', which should be num
    actualitem = item[0:numbegin]  #gets the actual item name
    actualitem2 = actualitem + ":" #adds a ":" at the end of item name
    coloncheck = False             #checks whether there's a colon in item
    coloncount = 0                 #checks if there's just 1 colon

    for i in range(0, len(item)):
        if item[i] == ":":
            coloncheck = True
            coloncount = coloncount + 1

    if coloncheck == False and coloncount != 1:
        resp.message("Item not stored: format incorrect")
    elif (quantity.isdigit() == False):
        resp.message("Item not stored: non-number entered")
    else:
        write = open("inventory.txt", "w")
        for line in lines:
            if actualitem2 not in line[:itemsize + 1]:
                write.write(line)
        write.close()

        with open("inventory.txt", "a") as f:
            f.write(item + "\n")
        f.close()
        resp.message(actualitem + ": " + quantity + " is stored")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
