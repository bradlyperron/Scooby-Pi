import rockBlock
import time
import fileHandler
import json 
 
from rockBlock import rockBlockProtocol
 
class Sensor (rockBlockProtocol):
    
    SLEEP_INTERVAL = 60
            
    def main(self):
            
        while(True):
		
	    def getJson (filename,value):
        
       		try:
            		data = fileHandler.read('/home/pi/logs/{}.json'.format(filename))
            		data = json.loads(data)
            		return data[value]
        	except:
            		return 0.0
       		
		
	    def emit(self, value):
            
	    	rb = rockBlock.rockBlock("/dev/ttyUSB1", self)
        	
            	rb.sendMessage("Td:" + str(time.time()) + ":" + str(depth) )
                                                                                  
            	rb.close()
		
	
	    depth = getJson('transducer', 'depth') 
            
            self.emit(depth)
                        
            time.sleep( self.SLEEP_INTERVAL)
                                

    def rockBlockTxStarted(self):
        print "rockBlockTxStarted"
        
    def rockBlockTxFailed(self):
        print "rockBlockTxFailed"
        
    def rockBlockTxSuccess(self,momsn):
        print "rockBlockTxSuccess " + str(momsn)
	
	
if __name__ == '__main__':
	Sensor().main()
