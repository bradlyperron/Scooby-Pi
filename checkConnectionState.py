import subprocess
import time
import os

state = ''
def pingTest():
	for i in range(6):
		ping = subprocess.call(["ping", "8.8.8.8", "-c1", "-W2", "-q"])
		if ping == 1:
			return False	
		else:
			continue
	return i 

def checkState():
	state = pingTest()
	if state >= 4:
		print("The state is Cell")
		return True
	else:
		for i in range(10):
			val = pingTest()
			if val >= 4:
				return True
			else:
				if i == 9 and val == False:
					print("The state is Sat")
					return False 


checkConnectionState = checkState()
if checkConnectionState == True:
	print("Starting cell sensors")
	os.system("python processes.py")
	

else:
	print("Starting sat sensors")
