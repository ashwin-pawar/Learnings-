# Installing Twilio Library

from twilio.rest import Client
from datetime import datetime, timedelta  #timedelta - used to calculate time diff & datetime - used to calculate date & time 
import time 

#setup client 

account_sid = 'AC0779ab03a4abgsa774dd4acbf35a0f2'
Auth_Token = '242476ef04f0fsdf34556f24f6b4f5b9'

client = Client(account_sid,Auth_Token)

# step 3 messge ky bhejna hai schduling

def send_whatsapp_message(recipient_number, message_body):
    try: 
        message = client.messages.create (
            from_='whatsapp:+18777804236',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
            
        )
        print(f'Message sent Successfully! Message SID {account_sid}')
    except Exception as e:
        print("An Error Occured",e)


name = input("Enter your Recipient Name =")  
recipient_number = input("Enter the Recipient Whatsapp Number with Country code (eg.+91) =")
message_body =input(f"Enter the Message you want to sent {name} =")


# step 5 parse date time calculate time delay (difference)

date_str = input("Enter the Date to send the Message (YYYY:MM:DD) =")
time_str =input("Enter the time to send the Messgae (HH:MM) in 24 hours = ")

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime =datetime.now()

# calculate difference (Delay) 

time_difference = schedule_datetime - current_datetime
delay_seconds =time_difference.total_seconds() 

if delay_seconds <=0:
    print("The Specified time is in the Past, Please enter Future time and date = ")
else:
    print(f"Message Schduled to be sent {name} at {schedule_datetime}.")


    #wait until the scheduled time 
    time.sleep(delay_seconds) 

    #send message
    send_whatsapp_message(recipient_number,message_body) 