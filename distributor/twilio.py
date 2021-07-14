import requests
import os

# Twilio SMS service.

SMS_URL = 'https://api.twilio.com/2010-04-01/Accounts/'
SMS_SID = os.environ['SMS_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
SENDER_NO = os.environ['SENDER_NO']

#Note, comma-separated list of devices.
PHONE_NO = os.environ['PHONE_NO'].split(',')

def distribute(msg_body):
    for phone_no in PHONE_NO:
        request_body = {
            "From" : SENDER_NO,
            "To" : phone_no,
            "Body" : msg_body
        }

        response = requests.post(
            ''.join([
                SMS_URL,
                SMS_SID,
                '/Messages.json'
            ]),
            auth = (
                SMS_SID,
                AUTH_TOKEN
            ),
            data = request_body
        )

        print(response.status_code)
        print(response.text)

