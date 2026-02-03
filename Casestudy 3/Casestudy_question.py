
'''Hospital Management System – Web, API & Robot Framework Automation

Problem Statement
A hospital wants to automate testing for its Hospital Management System, which includes:
A web portal for patient registration
REST APIs for patient records
Automated testing using Pytest and Robot Framework

Objectives
Students should:
Work with REST APIs and Web applications
Automate API tests using requests
Parse HTML content
Perform JSON serialization/deserialization
Implement Robot Framework automation
Execute tests via command line

System Components

1. Patient REST API (Flask)
HTTP Verb
Endpoint
Description
GET
/api/patients
Fetch all patients
POST
/api/patients
Register a patient
GET
/api/patients/
Get patient details
PUT
/api/patients/
Update patient info


2. Web Page (HTML)
Patient Registration Form:
Patient Name
Age
Gender
Contact Number
Disease
Doctor Assigned
Form submits data to backend REST API.

Automation Tasks
🔹 API Automation (Python + requests)
Students must:
Send GET and POST requests
Pass headers and request body
Validate API responses
Deserialize JSON responses
Handle negative test cases

🔹 Web Scraping Task
Use:
BeautifulSoup / lxml
Extract from patient list page:
Patient name
Age
Disease
Assigned doctor

Pytest Automation Requirements
Unit tests for API endpoints
API fixtures
conftest.py usage
Parameterized tests for multiple patients
Skip and xfail tests
Parallel execution (pytest-xdist)
Generate HTML reports

Robot Framework Automation
Tasks to Perform:
Install Robot Framework & Selenium Library
Write test cases using keyword-driven approach
Implement data-driven testing for patients
Automate:
Browser launch
Text field input
Radio button & checkbox selection
Dropdown handling
Implement suite setup & teardown
Execute tests via command line
'''
