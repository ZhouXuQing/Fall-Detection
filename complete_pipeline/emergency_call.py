# Use service provider twilio to send a message 

# Note: To run this code, need to enter 'pip install twilio' in the terminal
#       to install twilio package. And type 'python twilio.py' in the 
#       terminal to send the message.
from twilio.rest import Client

def send_text_message (phone_number):
    # After register in twilio, get the account_dis and auth_token
    account_sid = 'ACf0d10f5677203404125592fb89ec6324'
    auth_token = 'dd0ee1161a68fc65b34542e26a029896'
    # Set up a client to send message
    client = Client(account_sid, auth_token)
    # The message content
    message_content = 'Emergency!!!'
    # The message object, which contains the message content, 
    # the phone numbers that receive or send the message
    message = client.messages.create(body=message_content,
                                     from_='+12015791999',
                                     to=phone_number)

if __name__ == "__main__":
    # phone_number format: [+][country code][phone number including area code]
    phone_number = '+14109728480'
    send_text_message(phone_number)
