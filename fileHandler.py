def write(filename, data, lock):
    lock.acquire()
    with open(filename,'w') as f:
        f.write(data)
    lock.release()

def read(filename,lock):
    lock.acquire()
    with open(filename,'r') as f:
        data = f.read()
    lock.release()
    return data
