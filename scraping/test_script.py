import scraper as sp
import pandas as pd

# Select Wasatch Top 150 Trails
df = sp.topTrail_url("https://www.alltrails.com/parks/us/utah/uinta-wasatch-cache-national-forest", 150)

# Setting up the Page detail scraping
cell = []
ct = 0
for urls in df['Urls']:
    cells = sp.page_details(urls)
    cell.append(cells)
    ct += 1
    print(ct)
    
ds = pd.DataFrame.from_records(cell, columns=['Title','Diff','Reviews','Coordinates'])
