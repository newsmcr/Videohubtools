import socket
import sys
import time
import RPi.GPIO as GPIO

#establish GPIOS
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Establish TCP/IP sockets
sockvcs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets with devices
server_address = ('192.168.1.60', 9990)
sockvcs.connect(server_address)
time.sleep(0.4)
data = sockvcs.recv(8888)


#Define Output
Xout = 15
#Define mom input
Xin = 0

#==========================
#DEFINIERE ROUTINEN
#==========================
		
def routine2():
	#hier werden erstmal eventuelle daten aus dem script der tasten 1-14 geloescht.
	sockvcs.send("video output routing:\n\n")
	time.sleep(0.1)
	data = sockvcs.recv(8888)
	#hier beginnt das script mit der abfrage des routings
	sockvcs.send("video output routing:\n\n")
	time.sleep(0.1)
	outrouting = sockvcs.recv(4096)
	outrouting = outrouting.split('\n')
#	print(outrouting)
	#delete first rows
	i = 0
	while i <> 3:
		a = outrouting.pop(0)
		i += 1
	#Display output routing
	i = 0
	while i <> (Xout + 1):
		ausgabe = outrouting[i].split(' ')
		i += 1
		if (int(ausgabe[0]) == Xout):
			Xin = (ausgabe[1])
	#Hier wird Xin an das Modul zurueckgegeben - Passiert das nicht, wird der aktuelle input nicht richtig ausgelesen 
	#und schaltet nach druck der tasten 1-14 nicht an der stelle weiter sondern den input den Xin in den Anweisungen
	#fuer Taste 15 oder 16 hatte
	return Xin

#==========================
#BEGINN PROGRAMMSCHLEIFE
#==========================

routine2()
while True:
	#Button15
	if(GPIO.input(10) == 0):
		Xin = routine2();
		print(Xin)
		Xin = int(Xin)-1
		if(Xin < 0):
			Xin = 71
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(Xout) + " " + str(Xin) + "\n\n")
		print("VIDEO OUTPUT ROUTING:\n" + str(Xout) + " " + str(Xin) + "\n\n")
		time.sleep(0.1)
		data = sockvcs.recv(8888)
	#Button16
	if(GPIO.input(24) == 0):
		Xin = routine2();
		Xin = int(Xin)+1
		if(Xin > 71):
			Xin = 0
		sockvcs.send("VIDEO OUTPUT ROUTING:\n" + str(Xout) + " " + str(Xin) + "\n\n")
		print("VIDEO OUTPUT ROUTING:\n" + str(Xout) + " " + str(Xin) + "\n\n")
		time.sleep(0.1)
		data = sockvcs.recv(8888)

print 'Programm beendet.'
sockvcs.close()
