from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9ded0d8fee59979d89fa87339fb58ded"
# Your Auth Token from twilio.com/console
auth_token  = "e1fca826e799d8b352afdac3e7a2be5d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16143523456", 
    from_="+13608690243",
    body="Finished this chapter beep! Onto the next... DK was good too!")

print(message.sid)
