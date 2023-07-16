from twilio.rest import Client

account_sid = <acc_sid>
auth_token = <auth_token>
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=<number given by twilio with country code>,
  body=<your message>,
  to=<your number>
)

print(message.sid)
print('SMS sent successfully.')