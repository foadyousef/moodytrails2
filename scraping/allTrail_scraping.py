from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

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
date = []
for user in users:
    dt = user.find_all('span', attrs={"subtext pull-right"})
    print(dt[0].meta['content'])
    date.append(dt[0].meta['content'])

# Comments
coms = []
for user in users:
    ct = user.find_all('p', attrs={'xlate-google'})
    print(ct[0].text)
    coms.append(ct[0].text)
    
# Tags
ts = []
for user in users:
    tgs = user.find_all('span', attrs={'small active rounded'})
    print(len(tgs))
    if len(tgs) != 0:
        tl=[]
        for i in tgs:
            print(i.text)
            t = i.text
            tl.append(t)
    else:
        tl=[]
        tl.append("")
    ts.append(tl)


df = pd.DataFrame(list(zip(date, ts, coms)), columns=['Date','Tags','Comments'])