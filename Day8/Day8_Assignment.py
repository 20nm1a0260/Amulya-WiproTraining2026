
#! Question 1 – Web Interaction & REST API Consumption

#& Working with Web & APIs, Automation/Web interaction, requests library, Basics of REST API

'''
Write a Python program that:			
			
1. Uses the requests library to send a GET request to a public REST API (e.g., users or posts API)			
			
2. Sends custom headers with the request			
			
3. Parses the JSON response and extracts specific fields			
			
4. Serializes the extracted data and saves it into a JSON file			
			
5. Handles HTTP errors using proper exception handling.			
'''

import requests

import json

url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Requests-App"
}

try:
    response=requests.get(url,headers=headers)
    
    response.raise_for_status()

    users=response.json()

    extracted_data=[]
    
    for user in users:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        })
        
    with open("Assignment/DAY8/users_data.json", "w") as file:
        json.dump(extracted_data, file, indent=4)   
        
    print("data saved successfully")

except requests.exceptions.HTTPError as e:
    print("HTTP Error :",e) 

except requests.exceptions.RequestException as e:
    print("HTTP Error : ",e)
    
#! Question 2 – HTML Parsing & Data Extraction

#& Parsing HTML (BeautifulSoup, lxml), Web automation basics

'''
Write a Python program that:

1. Fetches an HTML webpage using the requests library

2. Parses the HTML using BeautifulSoup with the lxml parser

3. Extracts:

Page title

All hyperlinks

Specific table or list data

4. Converts the extracted data into JSON format

5. Saves the output into a file for further automation or analysis

'''
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

extracted_data={
    "page_title":soup.title.text,
    "Total_links":len(href),
    "links":href,
    "table_data":data
}

with open("Assignment/DAY8/parsinghtml.json","w")  as file:
    json.dump(extracted_data,file,indent=4)
print("Data extracted successfully") 
