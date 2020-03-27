#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("wx2dx.stormstown", "4YU+W]8swswj")

#Send the mail
msg = "
Hello!" # The /n separates the message from the headers
server.sendmail("wx2dx.stormstown@gmail.com", "bill.smith@wx2dx.net", msg)
