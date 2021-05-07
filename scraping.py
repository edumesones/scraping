
"""
Created on Fri May  7 16:15:21 2021

@author: egzlz
"""
"https://www.youtube.com/watch?v=Nz1zPkiHcbg&t=24s fuente"


from bs4 import BeautifulSoup
import numpy as np
import requests
import urllib.request

import pandas as pd
import time
authors=[]
dates=[]
statements=[]
sources=[]
targets=[]

def scrape_website(page_number):
    page_num=str(page_number)
    URL="https://www.politifact.com/factchecks/list/?page="+page_num
    webpage=requests.get(URL)
    soup=BeautifulSoup(webpage.text,'html.parser')
    statement_footer=soup.find_all("footer",attrs={"class":"m-statement__footer"})
    statement_qote=soup.find_all("div",attrs={"class":"m-statement__quote"})
    statement_meta=soup.find_all("div",attrs={"class":"m-statement__meta"})
    target=soup.find_all("div",attrs={"class":"m-statement__meter"})
    for i in statement_footer:
        link1=i.text.strip()
        name_and_date=link1.split()
        first_name=name_and_date[1]
        last_name=name_and_date[2]
        full_name=first_name +' '+last_name
        month=name_and_date[4]
        day=name_and_date[5]
        year=name_and_date[6]
        date=month+ " "+day+" "+year
        dates.append(date)
        authors.append(full_name)
    for i in statement_qote:
        link2=i.find_all("a")
        statement_text=link2[0].text.strip()
        statements.append(statement_text)
    for i in statement_meta:
         link3=i.find_all("a")
         source_text=link3[0].text.strip()
         sources.append(source_text)
    for i in target:
        link4=i.find("div",attrs={"class":"c-image"}).find("img").get("alt")
        targets.append(link4)
n=22
for i in range(1,n):
   scrape_website(i)

data=pd.DataFrame(columns=["author","statement","source","date","target"])
data["author"]=authors
data["statement"]=statements
data["source"]=sources
data["target"]=targets
data["date"]=dates  
def fake(text):
    if text=="true" or text=="mostly-true":
        return 'RIAL BRO'
    else:
        return "FAKE SHITT"
data["RIAL OR NOT"]=data["target"].apply(fake)
    
    
    
        
     
    
    
    
    