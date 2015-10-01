#!/usr/bin/python
import RPi.GPIO as GPIO
import socket
import sys
import time
###################################################################
# insert in '/etc/crontab'
#@reboot root [/location/ofyourfile.py]
#for autostart
####################################################################
#insert
#
#
#establish GPIOS
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Establish TCP/IP sockets
#vcs --> Switcher
sockvcs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.1.60', 9990)
sockvcs.connect(server_address)
time.sleep(0.4)
data = sockvcs.recv(8888)

#Define switcher Output

#Define each input
#
#		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " [input(logical)]" + "\n\n")
output = 15
#print('start')
while True:
	#Button01
	if(GPIO.input(21) == 0):
		#print('Button 1 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 42" + "\n\n")
		time.sleep(0.1)
	#Button02
	if(GPIO.input(20) == 0):
		#print('Button 2 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 43" + "\n\n")
		time.sleep(0.1)
	#Button03
	if(GPIO.input(26) == 0):
		#print('Button 3 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 44" + "\n\n")
		time.sleep(0.1)
	#Button04
	if(GPIO.input(16) == 0):
		#print('Button 4 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 45" + "\n\n")
		time.sleep(0.1)
	#Button05
	if(GPIO.input(19) == 0):
		#print('Button 5 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 46" + "\n\n")
		time.sleep(0.1)		
	#Button06
	if(GPIO.input(13) == 0):
		#print('Button 6 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 47" + "\n\n")
		time.sleep(0.1)		
	#Button07
	if(GPIO.input(12) == 0):
		#print('Button 7 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)		
	#Button08
	if(GPIO.input(6) == 0):
		#print('Button 8 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)		
	#Button09
	if(GPIO.input(5) == 0):
		#print('Button 9 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)		
	#Button10
	if(GPIO.input(7) == 0):
		#print('Button 10 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)		
	#Button11
	if(GPIO.input(8) == 0):
		#print('Button 11 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)		
	#Button12
	if(GPIO.input(11) == 0):
		#print('Button 12 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)		
	#Button13
	if(GPIO.input(25) == 0):
		#print('Button 13 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)		
	#Button14
	if(GPIO.input(9) == 0):
		#print('Button 13 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)		
	#Button15
	if(GPIO.input(10) == 0):
		#print('Button 13 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)
	#Button16
	if(GPIO.input(24) == 0):
		#print('Button 13 pressed')
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(output) + " 28" + "\n\n")
		time.sleep(0.1)
	
		
GPIO.cleanup()
