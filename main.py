# -*- coding: utf-8 -*-

import subprocess
import sys
import time
import os
from decimal import Decimal

count = 0
while count < 1:
	returned_temp =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_temp.py'])
	returned_temp = os.linesep.join([s for s in returned_temp.splitlines() if s])
	temp = Decimal(returned_temp) #string in decimal verwandeln
	
	returned_settemp =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_config.py'])
	returned_settemp = os.linesep.join([s for s in returned_settemp.splitlines() if s])
	settemp = Decimal(returned_settemp) #string in decimal verwandeln 
	
	print 'Aktuelle Temperatur:', temp
	print 'Eingestellte Temperatur:', returned_settemp	
	time.sleep(1)
	