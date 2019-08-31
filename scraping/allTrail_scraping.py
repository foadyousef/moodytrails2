from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get("https://www.alltrails.com/trail/us/south-carolina/north-augusta-greeneway-trail")

elem = driver.find_element_by_id("load_more")

while elem.text != '':
	try:
		elem.click()
		elem = driver.find_element_by_id("load_more")
	except:
		pass

soup = BeautifulSoup(elem, 'html.parser')
comments = soup.find_all()



print("hello")