import sys
import get_info
import ConfigParser
import os


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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/lib/firefox-esr/firefox-bin')


cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False		
driver = webdriver.Firefox(firefox_binary=binary, capabilities=cap, executable_path="/home/pi/geckodriver")
driver.get("http://python.org")

assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()



# element = driver.find_element_by_class_name("pull-right")
# or the following below 
# element = driver.find_element_by_name("q")
# element = driver.find_element_by_id("html ID name")
# element = driver.find_element_by_name("html element name")
#element = driver.find_element_by_xpath("//input[@id='passwd-id']")
#print(element)
#driver.close()


