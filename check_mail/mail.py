#!/usr/bin/python3
import smtplib
import datetime

<<<<<<< HEAD
MAIL_USER = "bill.smith@wx2dx.net"
MAIL_PASS = "oh5yU7CJJKP^"
=======
GMAIL_USER = "from@gmmail.com"
GMAIL_PASS = "PW"
>>>>>>> e85ff6435dabdaec1a3785bc5d0d45dcef8ba5d0

now = datetime.datetime.now()

text = 'Your mail box has been opened!!!\n\n'
text = text + 'Time: '+now.strftime("%H:%M:%S %Y-%m-%d")+'\n\n'

<<<<<<< HEAD
sent_from = MAIL_USER 
to = ['wx2dx_bill@verizon.net']
=======
sent_from = GMAIL_USER 
to = ['destination@gmail,com']
>>>>>>> e85ff6435dabdaec1a3785bc5d0d45dcef8ba5d0
subject = 'Mailbox Alert'
body = text

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
	server = smtplib.SMTP('mail.wx2dx.net', 587)
	server.starttls()

	server.login(MAIL_USER, MAIL_PASS)

	server.sendmail(sent_from, to, email_text)

except Exception as e:
	print(e)

finally:
	server.quit()


 


