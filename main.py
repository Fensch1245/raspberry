# -*- coding: utf-8 -*-

import subprocess
import sys
import time
import os
import logging
from decimal import Decimal
from datetime import datetime

logging.basicConfig(filename='log.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

count = 0
while count < 1:
# Aktuelle Temperatur des Raumes auslesen
	returned_temp =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_temp.py'])
	returned_temp = os.linesep.join([s for s in returned_temp.splitlines() if s])
	temp = Decimal(returned_temp) #string in decimal verwandeln

# Eingestellte Temperatur aus Config auslesen
	returned_settemp =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_config.py'])
	returned_settemp = os.linesep.join([s for s in returned_settemp.splitlines() if s])
	settemp = Decimal(returned_settemp) #string in decimal verwandeln 
	
# Aus Config auslesen ob Heater gesteuert werden soll
	returned_activateheater =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_config_heater.py'])
	returned_activateheater = os.linesep.join([s for s in returned_activateheater.splitlines() if s])
	activate_heater = Decimal(returned_activateheater) #string in decimal verwandeln 

	if activate_heater <> 0:
# Status der Heizung (Sonoff) auslesen	
		returned_state =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_state.py'])
		returned_state = os.linesep.join([s for s in returned_state.splitlines() if s])
		state = Decimal(returned_state) #string in decimal verwandeln	
		print 'Status der Heizung:', state
	else:
		state = 1
		
		
	print 'Aktuelle Temperatur:', temp
	print 'Eingestellte Temperatur:', settemp	
	print 'Soll die Heizung gesteuert werden?', activate_heater
	
	if activate_heater <> 0:
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
		if state == 1:
			os.system("sudo python /home/pi/raspberry/toggle_state.py")
			state = 0
			
	time.sleep(5)
	