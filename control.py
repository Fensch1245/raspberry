import sys
import get_info
import ConfigParser
import os
from lxml import html
import requests

page = requests.get('http://192.168.2.102/')
tree = html.fromstring(page.content)



#This will create a list of buyers:
buyers = tree.xpath('//div[@id="l1"]/text_content()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print 'Buyers: ', buyers
print 'Prices: ', prices












# os.system("sudo python /home/pi/raspberry/ch_config.py DEFAULT set_temp 69")



