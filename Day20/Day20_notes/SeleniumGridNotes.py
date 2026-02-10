
#& =========================================================
#& 1️⃣ WHAT IS SELENIUM GRID?
#& =========================================================

#! Selenium Grid allows you to run Selenium tests:
#* On multiple machines
#* On multiple browsers
#* On multiple operating systems
#* In parallel

#! Main Goal: Speed + Cross-Browser Testing


#& =========================================================
#& 2️⃣ WHY SELENIUM GRID IS NEEDED?
#& =========================================================

#~ ❌ Without Grid:
# Chrome   → 30 mins
# Firefox  → 30 mins
# Edge     → 30 mins
# Total    → 90 mins 😩

#~ ✅ With Grid (Parallel Execution):
# Chrome + Firefox + Edge run together
# Total → 30 mins ⚡

#! Parallel execution saves time in large test suites


#& =========================================================
#& 3️⃣ CORE CONCEPTS
#& =========================================================

#& 🔹 HUB
#* Central controller
#* Receives test requests
#* Assigns tests to nodes

#& 🔹 NODE
#* Machine that runs browser
#* Has Chrome / Firefox / Edge
#* Registers to Hub


#& =========================================================
#& 4️⃣ SELENIUM GRID 4 ARCHITECTURE
#& =========================================================

#~ Internal Components (Grid 4):

#* Router        → Receives test request
#* Distributor   → Chooses suitable node
#* Session Map   → Tracks active sessions
#* Event Bus     → Internal communication
#* Node          → Executes the test

#! These components are handled internally


#& =========================================================
#& 5️⃣ GRID 3 vs GRID 4
#& =========================================================

#~ Grid 3:
#* Separate hub & node mandatory
#* JSON Wire Protocol
#* Limited UI
#* Less scalable

#~ Grid 4:
#* Standalone mode available
#* W3C Protocol
#* Modern UI Dashboard
#* More scalable


#& =========================================================
#& 6️⃣ GRID MODES
#& =========================================================

#& 🔹 1. Standalone Mode
#* Hub + Node in single command
#* Best for beginners

#& 🔹 2. Hub & Node Mode
#* Run hub and nodes separately

#& 🔹 3. Distributed Mode
#* Enterprise-level scaling


#& =========================================================
#& 7️⃣ INSTALLATION STEPS
#& =========================================================

#todo Step 1: Install Java (JDK 11+)
# Check version:
# java -version

#todo Step 2: Download selenium-server-4.x.x.jar

#todo Step 3: Start Grid
# java -jar selenium-server-4.x.x.jar standalone

#! Open Dashboard:
# http://localhost:4444/ui


#& =========================================================
#& 8️⃣ HOW PYTHON CONNECTS TO GRID
#& =========================================================

#~ Instead of:
# webdriver.Chrome()

#~ We use:
# webdriver.Remote()

#! Because browser runs remotely


#& =========================================================
#& 9️⃣ DESIRED CAPABILITIES
#& =========================================================

#* browserName
#* browserVersion
#* platformName
#* headless mode
#* logging preferences

# Example:
# options.add_argument("--headless")


#& =========================================================
#& 1️⃣1️⃣ PARALLEL EXECUTION
#& =========================================================

#todo Install:
# pip install pytest pytest-xdist

#todo Run:
# pytest -n 4

#! This runs 4 tests simultaneously


#& =========================================================
#& 1️⃣2️⃣ REAL COMPANY USAGE
#& =========================================================

#* CI/CD pipelines
#* Jenkins
#* GitHub Actions
#* Cloud environments
#* Cross-browser testing


#& =========================================================
#& 1️⃣3️⃣ SELENIUM GRID WITH DOCKER
#& =========================================================

#~ Modern companies use Docker

# Example:
# docker run -d -p 4444:4444 selenium/standalone-chrome

#! Benefits:
#* Easy scaling
#* No dependency issues
#* Cloud ready
#* DevOps friendly


#& =========================================================
#& 1️⃣4️⃣ SCALING STRATEGY
#& =========================================================

#~ Horizontal Scaling:
#* Add more nodes

#~ Cloud Scaling:
#* BrowserStack
#* Sauce Labs
#* LambdaTest


#& =========================================================
#& 1️⃣5️⃣ COMMON ERRORS
#& =========================================================

#~ SessionNotCreatedException
# Browser version mismatch

#~ Connection Refused
# Grid not running

#~ TimeoutException
# Node overloaded


#& =========================================================
#& 1️⃣6️⃣ ADVANTAGES
#& =========================================================

#* Faster execution
#* Parallel testing
#* Cross-browser testing
#* Cross-platform testing
#* CI/CD friendly


#& =========================================================
#& 1️⃣7️⃣ DISADVANTAGES
#& =========================================================

#* Complex setup
#* Requires infrastructure
#* Debugging slightly harder


#& =========================================================
#& 1️⃣8️⃣ INTERVIEW QUESTIONS
#& =========================================================

#? What is Selenium Grid?
#? What is RemoteWebDriver?
#? Difference between Grid 3 and Grid 4?
#? How does parallel execution work?
#? What is Distributor in Grid 4?


#& =========================================================
#& 1️⃣9️⃣ FRAMEWORK STRUCTURE
#& =========================================================

# project/
# ├── tests/
# ├── pages/
# ├── conftest.py
# ├── requirements.txt
# └── pytest.ini

#! Grid URL usually configured inside conftest.py


#& =========================================================
#& 2️⃣0️⃣ WHEN TO USE GRID?
#& =========================================================

#* Test cases > 50
#* Cross-browser testing required
#* CI/CD execution
#* Enterprise automation


#& =========================================================
#& FINAL SUMMARY
#& =========================================================

#! Selenium Grid =
#* Remote execution
#* Parallel execution
#* Cross-browser testing
#* Scalable automation

#! Selenium is the engine.
#! Selenium Grid is the highway system.
