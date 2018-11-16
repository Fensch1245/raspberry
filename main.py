# -*- coding: utf-8 -*-

import subprocess
import sys
import time

count = 0
while count < 1:
	import get_temp
	returned_bin =  subprocess.check_output('get_temp.py'.split())
	print returned_bin
	time.sleep(2)