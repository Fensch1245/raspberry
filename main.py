# -*- coding: utf-8 -*-

import subprocess
import sys
import time


count = 0
while count < 1:
	returned_bin =  subprocess.check_output('/home/pi/raspberry/get_temp.py'.split())
	time.sleep(2)