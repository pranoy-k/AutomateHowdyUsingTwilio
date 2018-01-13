# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client
from time import sleep
# Find these values at https://twilio.com/user/account
account_sid = "AC8d1cc3f74f25a80deab06b057553d097"
auth_token = "1ae8e9dd7feb0c5ce9ebf683fc8f330a"
client = Client(account_sid, auth_token)

for i in range(10):
	message = client.api.account.messages.create(to="+19793243647", \
                                             from_="+19799852518",  \
                                             body="Hello AI course bhayya! Sent from Python")
	sleep(30)