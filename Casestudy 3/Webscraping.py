import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/api/patients"

response = requests.get(url)

data = response.json()

for patient in data:
    print("Name:", patient["patient_name"])
    print("Age:", patient["age"])
    print("Disease:", patient["disease"])
    print("Doctor:", patient["doctor_assigned"])
    print("---------------")