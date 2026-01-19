#~ subprocess is a Python module used to run system commands (terminal / shell commands) from Python code.


# import subprocess

# result = subprocess.run("echo Hello world",shell=True,capture_output=True,text=True)

# print(result.stdout)


#~ running files from here itself

# subprocess.run(("python","Python_Selenium_Notes/DAY4/Day4_16Jan2026.py"))
# subprocess.run(("python","Python_Selenium_Notes/DAY2/Day2_14Jan2026.py"))

#! Threading - Threading means running multiple tasks concurrently within a single process.

import threading

def task():
    print("Thread is running")

t=threading.Thread(target=task)

t.start()
t.join()

print("Main thread ends")


#! Virtual environment in python 

'''
A virtual environment is an isolated Python workspace that allows you to:

Install project-specific libraries

Avoid version conflicts

Keep system Python clean

👉 Each project gets its own dependencies.

'''

#* in one line - A virtual environment is an isolated Python environment used to manage project-specific dependencies without affecting system Python.