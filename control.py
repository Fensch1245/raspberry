import sys
import get_info
import ConfigParser
import os
from lxml import html
import requests

page = requests.get('http://192.168.2.102/')
tree = html.fromstring(page.content)



#This will create a list of buyers:
# buyers = tree.xpath('//*[@id="l1"]/text()')



# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')

# print 'Buyers: ', buyers
# print 'Prices: ', prices


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://192.168.2.102/')
list_of_elements = ["a", "button", "li", "nav", "ol", "span", "ul", "header", "footer", "section"]
for tag_name in list_of_elements:
    for element in browser.find_elements_by_tag_name(tag_name):
         print element









# os.system("sudo python /home/pi/raspberry/ch_config.py DEFAULT set_temp 69")



