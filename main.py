# -*- coding: utf-8 -*-

import get_temp

val = subprocess.check_output([sys.executable, "get_temp.py", "1"])

print val