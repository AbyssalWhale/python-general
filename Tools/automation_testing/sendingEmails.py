# mime - multipurpose internet mail extensions
# from string import Template - to replce params in HTML

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

EMAIL = "john@gmail.com"
PASSWORD = "PASSWORD"

TEMPLATE = Template(Path("emailTemplate.html").read_text())
TEMPLATE.substitute()

message = MIMEMultipart()
message["from"] = "OHA"
message["to"] = EMAIL
message["subject"] = "Test from python"

body = TEMPLATE.substitute({"name": "John"})
# set second parametr to 'html' to send html code
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("test_picture.png")))

with smtplib.SMTP(host="smpt.gmail.com", port=587) as smpt:
    # Hello message to smpt server. It always should must start from this
    smpt.ehlo()
    # to encrypt everything
    smpt.starttls()
    # test user
    smpt.login(EMAIL, PASSWORD)
    smpt.send_message(message)
    print("Sent...")
