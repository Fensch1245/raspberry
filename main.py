# -*- coding: utf-8 -*-

import subprocess
import sys
import time
import os
import logging
from decimal import Decimal
from datetime import datetime
import pyping

logging.basicConfig(filename='log.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

count = 0
while count < 1:
# Aktuelle Temperatur des Raumes auslesen
	returned_temp =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_temp.py'])
	returned_temp = os.linesep.join([s for s in returned_temp.splitlines() if s])
	temp = Decimal(returned_temp) #string in decimal verwandeln

# Eingestellte Temperatur aus Config auslesen
	returned_settemp =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_config.py', 'set_temp'])
	returned_settemp = os.linesep.join([s for s in returned_settemp.splitlines() if s])
	settemp = Decimal(returned_settemp) #string in decimal verwandeln 
	
# Aus Config auslesen ob Heater gesteuert werden soll
	returned_activateheater =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_config.py', 'activate_heater'])
	returned_activateheater = os.linesep.join([s for s in returned_activateheater.splitlines() if s])
	activate_heater = Decimal(returned_activateheater) #string in decimal verwandeln 
	
#Aus Config auslesen ob Temperatur geloggt werden soll
	returned_logtemp =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_config.py', 'log_temp'])
	returned_logtemp = os.linesep.join([s for s in returned_logtemp.splitlines() if s])
	log_temp = Decimal(returned_logtemp) #string in decimal verwandeln 

	r = pyping.ping('192.168.2.123')

	if r.ret_code == 0:
		response_heizung = 1
	else:
		response_heizung = 0

		
	if activate_heater == 1:
		if response_heizung == 1:
# Status der Heizung (Sonoff) auslesen	
			returned_state =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_state.py'])
			returned_state = os.linesep.join([s for s in returned_state.splitlines() if s])
			state = Decimal(returned_state) #string in decimal verwandeln	

	print ''
	print 'Update: ', datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print 'Soll die Temperatur geloggt werden? ', log_temp
	print 'Heizungssteuerung antwort: ', response_heizung	
	print 'Soll die Heizung gesteuert werden: ', activate_heater
	print 'Aktuelle Temperatur:', temp
	print 'Eingestellte Temperatur:', settemp	
	
	if log_temp == 1:
		logging.info(temp)
	
	#Heizungssteuerung
	if response_heizung == 1:
		if activate_heater == 1:
			if state == 0:
				if temp < (settemp - 2):
					print 'Heizung aktiviert', datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					logging.info('Heizung aktiviert')
					os.system("sudo python /home/pi/raspberry/toggle_state.py")
			else:
				if temp > (settemp - 2):
					print 'Heizung deaktiviert um :', datetime.now().strftime('%Y-%m-%d %H:%M:%S')
					logging.info('Heizung deaktiviert')
					os.system("sudo python /home/pi/raspberry/toggle_state.py")
		else:
			if response_heizung == 1:
				returned_state =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_state.py'])
				returned_state = os.linesep.join([s for s in returned_state.splitlines() if s])
				state = Decimal(returned_state) #string in decimal verwandeln	
				if state == 1:
					os.system("sudo python /home/pi/raspberry/toggle_state.py")
				
	
	time.sleep(5)
	