import sys
import get_info
import ConfigParser
import os
# from lxml import html
# import requests

# page = requests.get('http://192.168.2.102/')
# tree = html.fromstring(page.content)


# print(tree.text_content())
# #This will create a list of buyers:
# buyers = tree.xpath('//*[@id="l1"]')



# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')

# print 'Buyers: ', buyers
# print 'Prices: ', prices

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://tools.wmflabs.org/pageviews/?project=en.wikipedia.org&platform=all-access&agent=user&range=latest-20&pages=Star_Wars:_The_Last_Jedi")
# element = driver.find_element_by_class_name("pull-right")
# or the following below 
# element = driver.find_element_by_name("q")
# element = driver.find_element_by_id("html ID name")
# element = driver.find_element_by_name("html element name")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
print(element)
driver.close()








# os.system("sudo python /home/pi/raspberry/ch_config.py DEFAULT set_temp 69")



