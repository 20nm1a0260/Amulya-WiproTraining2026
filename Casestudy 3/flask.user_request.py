
import requests

BASE_URL = "http://127.0.0.1:5000/api/patients"

print("GET ALL PATIENTS")
response = requests.get(BASE_URL)
print(response.status_code)
print(response.json())


print("\nGET SINGLE PATIENT")
response = requests.get(f"{BASE_URL}/1")
print(response.status_code)
print(response.json())


print("\nPOST NEW PATIENT")

new_patient = {
    "patient_name": "Ravi",
    "age": 40,
    "gender": "male",
    "contact": "9998887776",
    "disease": "fever",
    "doctor_assigned": "Dr. Kumar"
}

response = requests.post(BASE_URL, data=new_patient)
print(response.status_code)
print(response.text)


print("\nUPDATE PATIENT")

updated_data = {
    "patient_name": "Ravi Updated",
    "age": 41,
    "gender": "male",
    "contact": "8887776665",
    "disease": "viral fever",
    "doctor_assigned": "Dr. Sharma"
}

response = requests.put(f"{BASE_URL}/2", json=updated_data)
print(response.status_code)
print(response.json())


print("\nDELETE PATIENT")

response = requests.delete(f"{BASE_URL}/2")
print(response.status_code)
print(response.json())
