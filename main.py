# -*- coding: utf-8 -*-

import subprocess
import sys
import time

count = 0
while count < 1:
	returned_bin =  subprocess.check_output('/home/pi/raspberry/get_temp.py'.split())
	print returned_bin
	time.sleep(2)