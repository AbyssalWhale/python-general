# mime - multipurpose internet mail extensions

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib
import smtplib

message = MIMEMultipart()
message["from"] = "OHA"
message["to"] = "olegenikus@gmail.com"
message["subject"] = "Test from python"
# set second parametr to 'html' to send html code
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Pat))

with smtplib.SMTP(host="smpt.gmail.com", port=587) as smpt:
    # Hello message to smpt server. It always should must start from this
    smpt.ehlo()
    # to encrypt everything
    smpt.starttls()
    # test user
    smpt.login("olegenikus@gmail.com", "password")
    smpt.send_message(message)
    print("Sent...")
