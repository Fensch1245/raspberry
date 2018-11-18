# -*- coding: utf-8 -*-

import subprocess
import sys
import time
import os
from decimal import Decimal

count = 0
while count < 1:
	returned_bin =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_temp.py'])
	returned_bin = os.linesep.join([s for s in returned_bin.splitlines() if s])
	temp = Decimal(returned_bin)
	print temp
	if temp > 23:
		print 'bigger'
	else:
		print 'smaller'
	
	time.sleep(2)
#	returned_bin =  subprocess.check_output('/home/pi/raspberry/get_temp.py'.split())
	