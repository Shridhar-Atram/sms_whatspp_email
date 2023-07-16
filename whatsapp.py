from twilio.rest import Client

account_sid = <acc_sid>
auth_token = <auth_token>
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:<number given by twilio with country code>',
  body=<message>,
  to='whatsapp:<your number>'
)

print(message.sid)
print("Message sent Successfully")