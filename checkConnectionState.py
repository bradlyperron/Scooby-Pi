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

status = pingTest()
print(status)
