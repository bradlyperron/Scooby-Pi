from subprocess import *
import sys
import subprocess
import os

identifier = ''
def ping():
    try:
        subprocess.check_output(["ping", "1.1.1.1"])
        return True                      
    except subprocess.CalledProcessError:
        return False

def check_state():
	state = ping() 
	print(state)
	if state == True:
		return True
	else:
		for i in range(3):
			val = ping()
			print(val)		
			if val == True:
				return True 
			else:
				print("not connected")
				if i == 2 and val == False:
					return False
					
			
status = check_state()
if status == True:
	#os.system('python3 processes.py')
	print("starting cell sensors")
	identifier = 'cell'
else:
	#os.system('python satelliteSensors.py')
	print("starting sat sensors")
	identifier = 'Sat'

print("the state is", identifier)
