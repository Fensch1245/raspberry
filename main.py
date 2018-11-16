# -*- coding: utf-8 -*-

import get_temp
import sys
import time




count = 0
while count < 5:
	val = get_temp.ret_val()
    print(val)
	time.sleep(0.5)