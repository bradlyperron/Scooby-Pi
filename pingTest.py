import subprocess
import time

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
			print(val)
			if val >= 4:
				print("Cell")
				return True
			else:
				print("not connected")
				if i == 9 and val == False:
					return False 


checkConnectionState = checkState()
if checkConnectionState == True:
	print("Starting cell sensors")

else:
	print("Starting sat sensors")
