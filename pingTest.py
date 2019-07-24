import subprocess
state = subprocess.call(["ping", "8.8.8.8", "-c1", "-W2", "-q"], stdout=open(os.devnull,'w'))
print(state)
