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
# Get tags
soup = BeautifulSoup(driver.page_source, 'html.parser')
tags = soup.find_all("span", attrs={"review-tags"})

tags[51]


soup.select("")
dates = [tms.find('meta') for tms in soup.find_all("div", class_="subtext pull-right")]

str(dates[1]).split(' ')[1].split("=")[1]

cnt = 0
for i in dates:
    if i != None:
        print(i)
        cnt+=1

print("hello")