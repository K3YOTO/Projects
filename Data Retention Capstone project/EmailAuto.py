import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror
from email.utils import COMMASPACE, formatdate


db_con = sqlite3.connect("Capstone.db")
db_cur = db_con.cursor()

db_cur.execute('''SELECT Email, InvoiceDate, Name FROM Invoices WHERE InvoiceDate < date('now','-7 years');''')
result = db_cur.fetchall()
print(result)

sender_email = "capstonebusinesses@gmail.com"
password = "jwzi bkew qygv rwfr"

server = smtplib.SMTP("smtp.gmail.com", port=587)
server.starttls()
server.login(sender_email, password)

for receiver_email,reciever_invoice,reciever_name in result:
    # Email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Data Deletion Notification"

    body = "Dear User,\nThis is to inform you that your data will be deleted within 30 days from our database.\n If you would you like a copy of your data " \
       "you can download it using the following link: <a href='http://yourwebsite.com/data_download'>Download Data</a>"

    message.attach(MIMEText(body, "html"))
    text = message.as_string()
    try:
        server.sendmail(sender_email, receiver_email, text)
        print(f"Successfully sent email to: {receiver_email}")
    except smtplib.SMTPException:
        print(f"Error while sending email to: {receiver_email}")

    
print("No Further invoices requiring emails, Data is now scheduled for deletion")