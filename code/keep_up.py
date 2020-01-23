from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://moodytrails.herokuapp.com/')
while True:
    time.sleep(1800)
    driver.refresh()
driver.quit()