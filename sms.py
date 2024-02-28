from twilio.rest import Client

account_sid = 'AC23a06e5f76dc3875f574aeb6ec2e1da5'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG5adf5ff619733db07535802d31be77e3',
  body='Your appointment date is 23/05/2024',
  to='+254741559592'
)

print(message.sid)