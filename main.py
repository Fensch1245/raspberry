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
	
	
	print 'Aktuelle Temperatur:', temp
		
	time.sleep(2)
	