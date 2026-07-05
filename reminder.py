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
patient_number = os.getenv('patient_number')
client = client(account_sid, auth_token)
# 3. functions 
def send_reminder(patient_name,medicine): 
    """Sends a formatted medication reminder via Twilio"""

try:
    print(f"Sending messages to {patient_name}...")

    #implementing 'Messaging_service_sid'
    message = client.messages.create(
        body=f"Hello {patient_name}, it is time for your {medicine}",
        from_='SMART MEDICATOR', 
        to=patient_number
    )
    print(f"Success! Message sent to {patient_name}. SID: {message.sid}")

    #ERRORS
except TwilioRestException as e:
    print(f"An error occurred: {e}")
