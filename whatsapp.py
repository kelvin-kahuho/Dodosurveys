from twilio.rest import Client

account_sid = 'AC23a06e5f76dc3875f574aeb6ec2e1da5'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+254741559592'
)

print(message.sid)


from twilio.rest import Client

account_sid = 'AC23a06e5f76dc3875f574aeb6ec2e1da5'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='what do yu mean',
  to='whatsapp:+254741559592'
)

print(message.sid)