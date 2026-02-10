
#& =========================================================
#& SELENIUM GRID DOWNLOAD & SETUP
#& =========================================================

#? Download Selenium Grid:
#? https://www.selenium.dev/downloads/

#todo Download the selenium-server-4.x.x.jar
#todo Place it inside your project folder

#todo Install Java (JDK 11+ required)

# Check Java version:
# java -version


#& =========================================================
#& START SELENIUM GRID (STANDALONE MODE)
#& =========================================================

#* Open Command Prompt inside project folder

#! Run:
# java -jar selenium-server-4.40.0.jar standalone

#! After running, open:
# http://localhost:4444/ui

#todo Now run your pytest automation code


#& =========================================================
#& WHAT IS SELENIUM GRID USED FOR?
#& =========================================================

#~ Selenium Grid is mainly used to:
#* Connect different machines
#* Run tests in parallel
#* Execute across multiple browsers
#* Execute across multiple operating systems


#& =========================================================
#& RUNNING HUB & NODE ON SAME MACHINE
#& =========================================================

#~ To connect Hub and Node manually,
#~ we must run both commands separately.

#& -------------------------
#& START HUB
#& -------------------------

#! HUB COMMAND

'''
java -jar selenium-server-4.40.0.jar hub ^

--host localhost ^

--port 4444 ^

--publish-events tcp://localhost:4442 ^

--subscribe-events tcp://localhost:4443
'''

#& -------------------------
#& START NODE
#& -------------------------

#! NODE COMMAND

"""
java -jar selenium-server-4.40.0.jar node ^

--hub http://localhost:4444 ^

--publish-events tcp://localhost:4442 ^

--subscribe-events tcp://localhost:4443
"""


#& =========================================================
#& RUNNING HUB & NODE ON DIFFERENT MACHINES
#& =========================================================

#~ Scenario:
#* Machine 1 → Hub
#* Machine 2 → Node

#& -------------------------
#& MACHINE 1 → HUB
#& -------------------------

#! HUB COMMAND (Machine 1)

'''
java -jar selenium-server-4.40.0.jar hub ^

--host 0.0.0.0 ^

--port 4444 ^

--publish-events tcp://192.168.1.10:4442 ^

--subscribe-events tcp://192.168.1.10:4443
'''

#~ Note:
# 192.168.1.10 = IP address of Hub machine


#& -------------------------
#& MACHINE 2 → NODE
#& -------------------------

#! NODE COMMAND (Machine 2)

'''
java -jar selenium-server-4.40.0.jar node ^

--hub http://192.168.1.10:4444 ^

--publish-events tcp://192.168.1.10:4442 ^

--subscribe-events tcp://192.168.1.10:4443
'''

#~ Make sure:
#* Both machines are in same network
#* Firewall allows port 4444, 4442, 4443
#* Java installed on both machines


#& =========================================================
#& FINAL QUICK UNDERSTANDING
#& =========================================================

#! Standalone Mode → Easiest (Hub + Node together)
#! Hub Mode → Controls execution
#! Node Mode → Executes tests
#! Different Machines → Use Hub IP instead of localhost

#todo Always verify Grid UI after starting:
# http://<hub-ip>:4444/ui


#& -------------------------
#& Numpy
#& -------------------------

#run command pip install numpy
