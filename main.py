# -*- coding: utf-8 -*-

import subprocess
import sys
import time
import os

count = 0
while count < 1:


#	import get_temp
#	val = get_temp.ret_val()
#	print val
	returned_bin =  subprocess.check_output(['sudo', 'python', '/home/pi/raspberry/get_temp.py'])
	returned_bin = os.linesep.join([s for s in text.splitlines() if s])
	
	print returned_bin
	print type(returned_bin)
	# if returned_bin > 23
		# print 'bigger'
	# else
		# print 'smaller'
	
	time.sleep(2)
#	returned_bin =  subprocess.check_output('/home/pi/raspberry/get_temp.py'.split())
	