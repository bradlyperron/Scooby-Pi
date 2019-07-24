import subprocess

state = ''

def pingTest():
	ping = subprocess.call(["ping", "8.8.8.8", "-c1", "-W2", "-q"])
	return ping

state = pingTest()

if state == 0:
	print("The state is Cell")
else:
	print("The state is Sat")


