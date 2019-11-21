import pandas as pd
import requests
from bs4 import BeautifulSoup

req=requests.get('http://ntry.com/stats/ladder/date.php')
html=req.text
soup=BeautifulSoup(html,'html.parser')

columns=soup.select('#stats-list > thead > tr > th')
columnlist=[]
for column in columns:
    columnlist.append(column.text)
df=pd.DataFrame(columns=columnlist)


contents=soup.select('#stats-list > tbody')
print(contents)
dfcontent=[]
alldfcontents=[]

for content in contents:
    tds=content.find_all("tr")
    for td in tds:
        dfcontent.append(td.text)
    alldfcontents.append(dfcontent)
    dfcontent=[]

test = soup.select('#round-history')
print(test)
# for a in test:
    # print(a)
print(test.find_all('tr'))
# all_divs = test.find_all("tr")
# print(all_divs)
# print(test)

#round-history