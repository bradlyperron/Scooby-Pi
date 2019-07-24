import subprocess

state = ''
def pingTest():
	ping = subprocess.call(["ping", "8.8.8.8", "-c1", "-W2", "-q"])
	return ping

while True:
	ping = pingTest()
	print(ping)
# def checkState():
# 	state = pingTest()
# 	if state == 0:
# 		print("The state is Cell")
# 		return True
# 	else:
# 		for i in range(3):
# 			val = pingTest()
# 			print(val)
# 			if val == 0:
# 				print("Cell")
# 				return True
# 			else:
# 				print("not connected")
# 				if i == 2 and val == False:
# 					return False 



# if checkConnectionState == True:
# 	print("Starting cell sensors")

# else:
# 	print("Starting sat sensors")
