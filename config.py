import os

class config:
    def __init__(self):
        read = open("credentials.txt", "r")
        for line in read:
            if('admin_username' in line):
                self.admin_username = line.split("=",1)[1].replace("\n", "")
                print(self.admin_username)
            elif('admin_apikey' in line):
                 self.admin_apikey = line.split("=",1)[1].replace("\n", "")
                 print(self.admin_apikey)
            elif('twilio_account_sid' in line):
                self.twilio_account_sid = line.split("=",1)[1].replace("\n", "")
                print(self.twilio_account_sid)
            elif('twilio_auth_token' in line):
                self.twilio_auth_token = line.split("=",1)[1].replace("\n", "")
                print(self.twilio_auth_token)
            elif('twilio_phone_number' in line):
                self.twilio_phone_number = line.split("=",1)[1].replace("\n", "")
                print(self.twilio_phone_number)
        read.close()