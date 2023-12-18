import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Getting input
get_DLC = input("What DLC do you want? ")

# Setting key/Emails
def Make_Key():
    Looped = 0
    AmountOfKeyChar = 17
    Key = ""

    while Looped < AmountOfKeyChar:
        RandomAlphabet = random.choice(string.ascii_letters)
        RandomNumber = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        Key += f"{RandomAlphabet}{RandomNumber}"
        Looped += 1

    return Key

# Function to send email
def send_email(subject, body, to_email, key):
    sender_email = "pythonbot665@gmail.com"
    sender_password = "dbmj mcyu lpks vktb"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    body_with_key = f"{body}\n\nDLC Key: {key}"
    message.attach(MIMEText(body_with_key, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()

# Main Handling
if get_DLC == "Police Interaction":
    Gmail = input("Enter your Gmail address: ")
    Key = Make_Key()
    send_email("Key for DLC", """Hello, you requested a key for a DLC in a game named 'Crime Filer'.
If this is not you, please ignore this. More Information on """, Gmail,Key)
    
    Needed_Key = input("Enter the key sent to your email: ")

    if Needed_Key == Key:
        with open("ActiveDLC.txt","a") as f:
            f.write("""Do not modify this txt file as it is breaking the rules!
                    
        Police: True\n""")
        print("You have unlocked this DLC.")

    else:
        print("Wrong Key! Try Again.")

elif get_DLC == "Impossible":
    Gmail = input("Enter your Gmail address: ")
    Key = Make_Key()
    send_email("Key for DLC", """Hello, you requested a key for a DLC in a game named 'Crime Filer'. If this is not you, please ignore this.""", 
               Gmail,Key)
    
    Needed_Key = input("Enter the key sent to your email: ")

    if Needed_Key == Key:
        with open("ActiveDLC.txt","a") as f:
            f.write("Impossible: True\n")
        print("You have unlocked this DLC.")

    else:
        print("Wrong Key! Try Again.")