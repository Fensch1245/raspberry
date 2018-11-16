# -*- coding: utf-8 -*-

import subprocess
import sys
import time

count = 0
while count < 1:
	import get_temp
	print get_temp.main()
	time.sleep(2)