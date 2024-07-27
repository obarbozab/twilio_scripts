import os
from twilio.rest import Client
import time
from dotenv import load_dotenv
import json

load_dotenv() # load environment variables from env file

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(account_sid,auth_token)

twilio_response = client.messages.create(
  #from_='+18017972087',
  from_= '+12058833479',
  body =f'test',
  #to ='+16168284433'
  to = os.environ.get('my_number')
  #to = '+12542218604'
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
# load api response 
api_response = client.http_client._test_only_last_response

# Parse the JSON response content
response_data = json.loads(api_response.content)


print("---------------------------------------------------------------------------------------")
print(f" Message SID: {twilio_response.sid} | Status: {twilio_response.status} | Error code: {twilio_response.error_code} | Error message: {twilio_response.error_message}")
print("---------------------------------------------------------------------------------------")
print(client.http_client._test_only_last_request)
print("---------------------------------------------------------------------------------------")
for key, value in response_data.items():
  print(f"{key}: {value}")
print("---------------------------------------------------------------------------------------")
print(f"Request SID: {client.http_client._test_only_last_response.headers['twilio-request-id']}") # just the request SID '''
print("---------------------------------------------------------------------------------------")
