#!/usr/bin/python3

import spidev, time
import time
import datetime
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
	adc = spi.xfer2([1, (8 + channel) << 4, 0])
	data = ((adc[1]&3) << 8) + adc[2]
	return data

# Function to convert data to voltage level
# rounded to specified number of decimal places
def ConvertVolts(data,places):
	volts = (data * 3.3) / float(1023)
	volts = round(volts,places)
	return volts

mySendMail = '/home/pi/projects/mailbox/mail.py'
myResetChime = '/home/pi/projects/mailbox/reset.py'

# print ("Check mail was run.")
reading = ReadChannel(0)
voltage = ConvertVolts(reading,2)
#	print("Reading=%d\tVoltage=%.2f" % (reading, voltage))
# If voltage is greater than or equal to 0.75 V then send an e-mail
if (voltage >= 0.75):
	os.system(mySendMail)
	now = datetime.datetime.now()
	print("Mailbox was opened at: ")
	print(now.strftime('%H:%M %Y-%m-%d'))
	time.sleep(60)
	os.system(myResetChime)
	print("Mailbox Chime has been reset.")
