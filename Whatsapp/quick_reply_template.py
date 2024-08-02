import os
from twilio.rest import Client
from dotenv import load_dotenv
import json

load_dotenv() # load environment variables from env file

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(account_sid,auth_token)

twilio_response = client.messages.create(
    content_sid="HX2af507311fd99fbb57b3b93383ff6d6f",
    to= os.environ.get("my_wa_number"),
    from_='MGed2ab7fa9ab8d197b19404aad1b7524f',
        content_variables=json.dumps({
            '1': "Johnny Pardo",
            '2': "DragonCEM",
            '3': "Smoky Mangoose",
            '4': "Google Ads"
            }),
)

# load api response 
api_response = client.http_client._test_only_last_response

# Parse the JSON response content
response_data = json.loads(api_response.content)

print("---------------------------------------------------------------------------------------")
print(f" Message SID: {twilio_response.sid} | Error code: {twilio_response.error_code} | Error message: {twilio_response.error_message}")
print("---------------------------------------------------------------------------------------")
print(client.http_client._test_only_last_request)
print("---------------------------------------------------------------------------------------")
for key, value in response_data.items():
  print(f"{key}: {value}")
print("---------------------------------------------------------------------------------------")
print(f"Request SID: {client.http_client._test_only_last_response.headers['twilio-request-id']}") # just the request SID '''
print("---------------------------------------------------------------------------------------")