import os
from twilio.rest import Client
import json
import random

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

def generate_otp(length=6):
  """Generates a random OTP of specified length."""
  otp = ''.join(str(random.randint(0, 9)) for _ in range(length))
  return otp

otp = generate_otp()

wa_number = os.getenv('my_wa_number')

def send_verify_otp(wa_number,otp):
    message = client.messages.create(
        content_sid='HX24415a28ee1d99481c081c1e7a938014',
        from_='MGed2ab7fa9ab8d197b19404aad1b7524f',
        content_variables=json.dumps({
            '1': otp
            }),
        to = wa_number
    )
    print("----------------------------------------")
    print(f" Message SID: {message.sid}")
    print("----------------------------------------")
    print(client.http_client._test_only_last_request)
    print("----------------------------------------")
    print(client.http_client._test_only_last_response)
    print("----------------------------------------")
    print(client.http_client._test_only_last_response.headers['twilio-request-id']) # just the request SID 

send_verify_otp(wa_number,otp)