# -*- coding: utf-8 -*-

import subprocess
import sys
import time
import os
from decimal import Decimal

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

# Status der Heizung (Sonoff) auslesen	
	returned_state =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_state.py'])
	returned_state = os.linesep.join([s for s in returned_state.splitlines() if s])
	state = Decimal(returned_state) #string in decimal verwandeln	
	
	print 'Aktuelle Temperatur:', temp
	print 'Eingestellte Temperatur:', settemp	
	print 'Status der Heizung:', state
	
	if state == 0:
		if temp < (settemp - 2):
			os.system("sudo python /home/pi/raspberry/toggle_state.py")
	else:
		if temp > (settemp - 2):
			os.system("sudo python /home/pi/raspberry/toggle_state.py")
	
	time.sleep(3)
	