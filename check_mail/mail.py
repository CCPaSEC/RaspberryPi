#!/usr/bin/python3
import smtplib
import datetime

GMAIL_USER = "from@gmmail.com"
GMAIL_PASS = "PW"

now = datetime.datetime.now()

text = 'Your mail box has been opened!!!\n\n'
text = text + 'Time: '+now.strftime("%H:%M:%S %Y-%m-%d")+'\n\n'

sent_from = GMAIL_USER 
to = ['destination@gmail,com']
subject = 'Mailbox Alert'
body = text

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()

	server.login(GMAIL_USER, GMAIL_PASS)

	server.sendmail(sent_from, to, email_text)

except Exception as e:
	print(e)

finally:
	server.quit()


 


