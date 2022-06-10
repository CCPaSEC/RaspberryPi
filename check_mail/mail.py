#!/usr/bin/python3
import smtplib
import datetime

MAIL_USER = "bill.smith@wx2dx.net"
MAIL_PASS = "oh5yU7CJJKP^"

now = datetime.datetime.now()

text = 'Your mail box has been opened!!!\n\n'
text = text + 'Time: '+now.strftime("%H:%M:%S %Y-%m-%d")+'\n\n'

sent_from = MAIL_USER 
to = ['wx2dx_bill@verizon.net']
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


 


