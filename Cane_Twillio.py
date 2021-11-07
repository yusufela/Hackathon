import os
from twilio.rest import Client
from gpiozero import Button



#This allows us to use the Twilio API
account_sid=os.environ['AC5baa34701d78f745dd92b7f7974ec331'] 
auth_token=os.environ['ed99edd476879a1486c9f7a084033b04']
client = Client(os.environ['account_sid']
, os.environ['auth_token']
)
#set up the tilt switch on GPIO 14
tilt_switch = Button(14) # + will go to 5V and Signal to GPIO14  

if(tilt_switch.when_pressed): #the tilt switch falling indicates  
    message = client.messages.create(
                              body='Cane has fallen! Please check up on me.',
                              from_='+17792092758',
                              to='+13159824560'
                          )

print(message.sid)
