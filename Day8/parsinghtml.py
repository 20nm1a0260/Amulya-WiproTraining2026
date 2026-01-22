
import requests

from bs4 import BeautifulSoup

import json


#url="https://tutorialsninja.com/demo/"
url="https://www.w3schools.com/html/html_tables.asp"

response=requests.get(url)

soup=BeautifulSoup(response.text,"lxml")

#!title text

# print(soup.title.text) 

#! para text

# print(soup.p.text) if soup.p else "NO para found"

#! getting hyperlinks

for link in soup.find_all("a"): 
    href=link.get("href")
    

#! getting tables 

table=soup.find("table")

for row in table.find_all("tr"):
    cells = row.find_all(["th", "td"])
    data = [cell.text.strip() for cell in cells]

#! storing them
extracted_data={
    "page_title":soup.title.text,
    "Total_links":len(href),
    "links":href,
    "table_data":data
}

#! sending stored data into the json file to save locally

with open("Python_Selenium_Notes/DAY8/parsinghtml.json","w")  as file:
    json.dump(extracted_data,file,indent=4)
print("Data extracted successfully") 
