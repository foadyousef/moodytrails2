from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get("https://www.alltrails.com/trail/us/south-carolina/savannah-river-bluffs")

elem = driver.find_element_by_id("load_more")

while elem.text != '':
	try:
		elem.click()
		elem = driver.find_element_by_id("load_more")
	except:
		pass


# Reviews
soup = BeautifulSoup(driver.page_source, 'html.parser')
reviews = soup.find_all('div',attrs={"id":"reviews"})

# Users
users = reviews[0].find_all('div', attrs={"feed-item"})

# Dates
for user in users:
    dt = user.find_all('span', attrs={"subtext pull-right"})
    print(dt[0].meta['content'])

# Comments
for user in users:
    ct = user.find_all('p', attrs={'xlate-google'})
    print(ct[0].text)
    
# Tags
    
ctss = 0
ts = []
for user in users:
    tgs = user.find_all('span', attrs={'small active rounded'})
    ctss +=1
    for i in range(len(tgs)):
        print(tgs[i].text)
        t = tgs[i].text
        ts.append(t)
