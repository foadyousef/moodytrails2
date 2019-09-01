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

soup = BeautifulSoup(driver.page_source, 'html.parser')
comments = soup.find_all("span", attrs={"small active rounded"})
dates = [tms.find('meta', class_="conetent") for tms in soup.find_all("span", class_="subtext pull-right")]

dates[1]



print("hello")