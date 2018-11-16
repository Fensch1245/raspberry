# -*- coding: utf-8 -*-

import get_temp
import sys
import time



count = 0
while count < 1:
	val = get_temp.ret_val()
	print val
	del val
	time.sleep(2)