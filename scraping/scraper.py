# This the Scraper


def page_details(url):
    
    """
    Captures the following:
        Trail Diff
        Trail # of reviews
        Trailhead coordinate
    """
    
    from selenium import webdriver
    from bs4 import BeautifulSoup
    
    driver = webdriver.Firefox()
    driver.get(url)
    
    #Trail Diff
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    tdetail1 = soup.find_all('div',attrs={"id":"title-and-difficulty"})
    diff_lvl = tdetail1[0].span.text
    
    #Trail # reviews
    tdetail2 = soup.find_all('span',attrs={"itemprop":"reviewCount"})
    review_count = tdetail2[0].text
    
    # Trail head
    tdetail3 = soup.find_all('div',attrs={"class":"stats xlate-none"})
    thead = tdetail3[0].text
    
    driver.close()
    
    return [diff_lvl, review_count, thead]
    


def page_load(url):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import pandas as pd
    
    driver = webdriver.Firefox()
    driver.get(url)
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
        #print(dt[0].meta['content'])
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
    
    #close the driver
    driver.close()
    
    #Final Data Frame
    df = pd.DataFrame(list(zip(date, ts, coms)), columns=['Date','Tags','Comments'])
    return df