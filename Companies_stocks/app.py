import pandas as pd
import requests 
from bs4 import BeautifulSoup

url = 'https://ticker.finology.in/market/52-week-high'

r = requests.get(url)



soup =BeautifulSoup(r.text,'lxml')
  

## ----- table headers  
header = soup.find_all('th')

#print(header)
titles = []
for i in header:
    title = i.text
    titles.append(title)

df = pd.DataFrame(columns=titles)


##----table data

rows = soup.find_all("tr")
#print(rows)

for i in rows[1:]:
    data = i.find_all('td')
   # print(data)

    row = [tr.text for tr in data]
    #rint(row)

    l = len(df)

    df.loc[l] = row


df=df.drop('S.No.',axis=1)


df.to_csv('52_weeks_high dataset.csv',index=False)


