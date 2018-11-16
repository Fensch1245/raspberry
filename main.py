# -*- coding: utf-8 -*-


import sys
import time

count = 0
while count < 1:
	import get_temp
	val = get_temp.ret_val()
	print val
	time.sleep(2)