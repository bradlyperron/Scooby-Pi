import subprocess
import sys

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
		print("cellular connection")
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
					
			
x =check_state()
print("wabam")
print(x)

