import scraper as sp
import pandas as pd

# Select Wasatch Top 150 Trails
df = sp.topTrail_url("https://www.alltrails.com/parks/us/utah/uinta-wasatch-cache-national-forest", 150)
df = pd.read_csv("uinta-wasatch-cache-national-forest_Top150_Trails.csv")
# Setting up the Page detail scraping
cell = []
ct = 0
for urls in df['Urls']:
    cells = sp.page_details(urls)
    cell.append(cells)
    ct += 1
    print(ct)
    
ds = pd.DataFrame.from_records(cell, columns=['Title','Diff','Reviews','Coordinates'])

ddir = '/home/fyousef/Documents/moodytrails2/Data/'

tells = []
ct = 0
for url in df['Urls'][84:]:
    trail_detaisl = sp.page_load(url)
    nm = url.split("/")
    nm = nm[-1]
    trail_detaisl.to_csv(ddir+nm+'.csv')
    ct += 1
    print("###########"+"Trail# "+str(ct))