import os 
from dotenv import load_dotenv 
from twilio.rest import Client
import schedule 
import time 

# 1. load credentials 
load_dotenv()
# 2. Twilio 
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = client(account_sid, auth_token)
