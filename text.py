import configparser
import datetime
from twilio.rest import Client

# creds
ACCOUNT_SID = 'YOUR_ACCOUNT_SID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
PHONE_NUM = 'YOUR_TWILIO_PHONE_NUMBER'

# initializing twilio api
client = Client(ACCOUNT_SID, AUTH_TOKEN)

now_ = datetime.datetime.utcnow()
last_message_sid = None

def get_message():
    global last_message_sid

    # retrieving the latest SMS message
    try:
        message = client.messages.list(to='+18667940289', limit=1, date_sent_after=now_)[0]
        if message.sid != last_message_sid:
            last_message_sid = message.sid
            text = message.body
            # print(text)
        else:
            text = None
    except:
        text = None

    return text