import requests
from bs4 import BeautifulSoup
import csv
import pandas as p

url="https://www.flipkart.com/search?q=mobiles"
r=requests.get(url)


soup=BeautifulSoup(r.content,"html.parser" )


titles=soup.find_all('div' ,class_='_4rR01T')
ratings=soup.find_all('div',class_= '_3LWZlK')
reviews=soup.find_all('span',class_='_2_R_DZ')
prices=soup.find_all('div',class_='_25b18c')

mt=[]
mr=[]
mre=[]
mp=[]

for titles,ratings,rev,pri in zip(titles,ratings,reviews,prices):
    mt.append(titles.text)
    mr.append(ratings.text)
    mre.append(rev.text)
    mp.append(pri.text)

#saving data in csv

d={'mt':mt,'mr':mr,'mre':mre,'mp':mp}

model=p.DataFrame(data=d)

model.to_csv("mobilesdata.csv'")