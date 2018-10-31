import sys
import get_info
import ConfigParser
import ch_config


config = ConfigParser.ConfigParser()
config.read('config.ini')

print(config.get('DEFAULT', 'set_temp'))

ch_config.update_val('DEFAULT', 'set_temp', '25')

#print get_info.temp()



