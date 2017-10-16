class config:
    def __init__(self):
        self.admin_username = request.args.get('admin_username')

        self.admin_apikey = request.args.get('admin_apikey')

        self.twilio_account_sid = request.args.get('twilio_account_sid')

        self.twilio_auth_token = request.args.get('twilio_auth_token')

        self.twilio_phone_number = request.args.get('twilio_phone_number')