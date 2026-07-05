import os 
from dotenv import load_dotenv 
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import schedule 
import time 

patient_name = "ron"
medicine = "paracetamol"
scheduled_time = "10:00" 

# 1. load credentials 
load_dotenv()
print(f"SIS found: {os.getenv('TWILIO_ACCOUNT_SID')}, {os.getenv('TWILIO_AUTH_TOKEN')}, {os.getenv('Patient_number')}")
# 2. Twilio 
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
patient_number = os.getenv('Patient_number')
client = Client(account_sid, auth_token)
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

# scheduling the task
schedule.every().day.at(scheduled_time).do(send_reminder, patient_name, medicine)

#loop
print("system is running and waiting for schedule...")
while True:
    schedule.run_pending()
    time.sleep(1)