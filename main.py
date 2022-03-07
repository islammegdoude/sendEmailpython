import smtplib
import os
import imghdr
from email.message import EmailMessage

email_user = 'YOUR_EMAIL'
email_pass = 'YOUR_PASSWORD'
email_person = 'the_email_of_the_person_you_are_sending_it_to'
contacts = ['']
msg = EmailMessage()
msg['Subject'] = 'hak chofff'
msg['From'] = email_user
msg['To'] = email_person
msg.set_content("waaa3er ana chof chof ...")

# hada ll photo
#with open('islammegd.jpg', 'rb') as f:
#    file_data = f.read()
#    file_type = imghdr.what(f.name)
#    file_name = f.name
# hada ll pdf
files = ['Formations-Filière-Informatique-UMB-Msila.pdf']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_user, email_pass)
    smtp.send_message(msg)
