import sys
import get_info
import ConfigParser
import ch_config


config = ConfigParser.ConfigParser()
config.read('/home/pi/raspberry/config.ini')
ch_config.update_val('DEFAULT', 'set_temp', '25')



