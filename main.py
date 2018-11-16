# -*- coding: utf-8 -*-

import get_temp
import sys
import time

val = get_temp.ret_val()
print val


count = 1
while count < 1:
	val = get_temp.ret_val()
	print val
	time.sleep(2)