# -*- coding: utf-8 -*-

import subprocess
import sys
import time


count = 0
while count < 1:
	import get_temp
	val = get_temp.ret_val()
	print val
	time.sleep(2)
#	returned_bin =  subprocess.check_output('/home/pi/raspberry/get_temp.py'.split())
	