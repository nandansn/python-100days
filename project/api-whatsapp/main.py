import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['ACa233dbea0516e47f9b9a7571d2d790e8']
# auth_token = os.environ['7525e5ee727c23da3c3acf4376d56282']

account_sid = 'ACa233dbea0516e47f9b9a7571d2d790e8'
auth_token = '7525e5ee727c23da3c3acf4376d56282'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+918072321970',
                              to='whatsapp:+919003267101'
                          )

print(message.sid)