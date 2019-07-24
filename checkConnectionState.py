import subprocess
import time

state = ''
def pingTest():
	for i in range(4):
		num = 0
		ping = subprocess.call(["ping", "8.8.8.8", "-c1", "-W2", "-q"])
		if ping == 0:
			num += 1
		return num
		else:
			return False
	

status = pingTest()
print(status)
