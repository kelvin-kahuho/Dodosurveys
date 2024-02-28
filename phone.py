# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC23a06e5f76dc3875f574aeb6ec2e1da5"
auth_token = "4eea1e7181f75a572b20ebae050a5a35"
verify_sid = "VA27a2bdc06461ad48b7088af445798aa6"
verified_number = "+254741559592"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)