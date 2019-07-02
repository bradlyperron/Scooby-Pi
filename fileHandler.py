from filelock import FileLock

def write(filename, data):
	lock = FileLock(filename+'.lock')
	with lock:
		f = open(filename,'w')
		f.write(data)
		f.close()
		

def read(filename):
	lock = FileLock(filename+'.lock')	
	with lock:
		f = open(filename,'r')
		data = f.read()
		f.close()
	return data