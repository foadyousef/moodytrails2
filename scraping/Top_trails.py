from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get("https://www.alltrails.com/us/utah/hiking")


elem = driver.find_element_by_xpath("//*[@id='load_more']/a/div/h3")

# each load more loads 24 more trials. B/c I only need 200 top trails I will use a counter to stop the while loop!
cnt = 0
while cnt < 10:
    try:
        elem.click()
        elem = driver.find_element_by_xpath("//*[@id='load_more']/a/div/h3")
        time.sleep(3)
    
    except:
        pass
    
    cnt = cnt + 1
    
# Top trails
soup = BeautifulSoup(driver.page_source, 'html.parser')
trails = soup.find_all('li',attrs={"class":"sortable"})

# Trail name
nms = []
for trail in trails:
    nm = trail.div.div.div.h3.a.text
    nms.append(nm)

# Trail Urls:
urls = []
for trail in trails:
    url = trail.div['itemid']
    url = "https://www.alltrails.com"+url
    urls.append(url)
    

df = pd.DataFrame(list(zip(nms, urls)), columns=['Trail_Name','Urls'])

