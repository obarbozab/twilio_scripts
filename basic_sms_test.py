import os
from twilio.rest import Client
import time

#POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Messages

# MASON
#api_key = "SKcaf6c484883ab5c3cb02932396ef9e7e"
#api_secret = "xeae26GYLmRa70ZDY9zv30X6ClSfKjvD"
#account_sid = "ACfc35af18f88bfff0cf5310525ee802f8"

# MINE
#account_sid = 'ACb8eef81e158531b4d736f37687862342'
#auth_token = '90872975028b298ab8571513736fd73c'

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

#print(os.getenv("TWILIO_ACCOUNT_SID"))
#print(os.getenv("TWILIO_AUTH_TOKEN"))
#print (os.environ)
#api_key = os.getenv("TWILIO_API_KEY"),
#api_secret = os.getenv("TWILIO_API_SECRET")

#client = Client(api_key,api_secret,account_sid)

client = Client(account_sid,auth_token)

twilio_response = client.messages.create(
  #from_='+18017972087',
  from_= '+12058833479',
  body =f'help',
  #to ='+16168284433'
  #to = os.getenv('my_number')
  to = '+12542218604'
)

# Wait for a few seconds to allow the status to update
#time.sleep(5)  # Delays for 5 seconds. You can change the number to any amount of seconds you need.

# Fetch the message again to get the updated status
#message_updated = client.messages.get(twilio_response.sid).fetch()

# Print the final status, error code, and error message

'''print(f"Message SID: {message_updated.sid} | Final Status: {message_updated.status}")
if message_updated.error_code:
    print(f"Error Code: {message_updated.error_code}")
    print(f"Error Message: {message_updated.error_message}")
else:
    print("Message sent successfully")

'''
print("----------------------------------------")
print(f" Message SID: {twilio_response.sid} | Status: {twilio_response.status} | Error code: {twilio_response.error_code} | Error message: {twilio_response.error_message}")
print("----------------------------------------")
print(client.http_client._test_only_last_request)
print("----------------------------------------")
print(client.http_client._test_only_last_response)
print("----------------------------------------")
print(client.http_client._test_only_last_response.headers['twilio-request-id']) # just the request SID '''
